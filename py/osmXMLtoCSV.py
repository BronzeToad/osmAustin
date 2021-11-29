# ========================================================================= #
#   WGU - Udacity: Data Wrangling
#   OpenStreetMap - ATX
#   Prepare XML data for database import
# ========================================================================= #

import cerberus
import codecs
import csv
import pprint
import re
import xml.etree.ElementTree as eT
import os

import schema
from osmKeySurface import filter_surface, clean_surface
from osmKeyPostcode import filter_postcode, clean_postcode
from osmKeyCity import clean_city
from osmKeyBuilding import clean_building
from TicToc import TicToc
t = TicToc()

# ========================================================================= #
#                           Define Variables                                #
# ========================================================================= #

# define file paths
ROOT = '/Users/ajp/dsProjects/workspace/osmAustin/data/'
OSM_PATH = ROOT + 'austin_texas.osm'
# OSM_PATH = ROOT + 'sample_atx.osm'
# OSM_PATH = ROOT + 'small_sample_atx.osm'

NODES_PATH = ROOT + 'csv/nodes.csv'
NODE_TAGS_PATH = ROOT + 'csv/nodes_tags.csv'
WAYS_PATH = ROOT + 'csv/ways.csv'
WAY_NODES_PATH = ROOT + 'csv/ways_nodes.csv'
WAY_TAGS_PATH = ROOT + 'csv/ways_tags.csv'

# define regex strings
LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# define schema
SCHEMA = schema.schema

# set field order for csv export
NODE_FIELDS = [
    'id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp'
]

NODE_TAGS_FIELDS = [
    'id', 'key', 'value', 'type'
]

WAY_FIELDS = [
    'id', 'user', 'uid', 'version', 'changeset', 'timestamp'
]

WAY_TAGS_FIELDS = [
    'id', 'key', 'value', 'type'
]

WAY_NODES_FIELDS = [
    'id', 'node_id', 'position'
]


# ========================================================================= #
#                           Shape Function                                  #
# ========================================================================= #

def shape_element(element):
    """Shape node and way XML elements to Python dictionary"""

    way_attr_fields = WAY_FIELDS
    node_attr_fields = NODE_FIELDS
    problem_chars = PROBLEMCHARS
    default_tag_type = 'regular'

    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []

    if element.tag == 'node':
        for i in node_attr_fields:
            node_attribs[i] = element.get(i)

        for j in element.iter('tag'):
            key = j.get('k')
            val = j.get('v')

            # drop problematic tags
            if re.match(problem_chars, key):
                continue
            if key == 'addr:state' and val != 'TX':
                continue
            if key == 'addr:postcode':
                if filter_postcode(val):
                    continue
            if key == 'surface':
                if filter_surface(val):
                    continue

            # cleaning functions
            if key == 'addr:postcode':
                val = clean_postcode(val)
            elif key == 'addr:city':
                val = clean_city(val)
            elif key == 'building':
                val = clean_building(val)
            elif key == 'surface':
                val = clean_surface(val)

            mat = re.match(LOWER_COLON, key)

            if mat:
                key_split = re.split(':', key, maxsplit=1)
                tags_dict = {
                    'id': node_attribs['id'],
                    'key': key_split[1],
                    'value': val,
                    'type': key_split[0]
                }

            else:
                tags_dict = {
                    'id': node_attribs['id'],
                    'key': key,
                    'value': val,
                    'type': default_tag_type
                }

            tags.append(tags_dict)

        return {
            'node': node_attribs,
            'node_tags': tags
        }

    elif element.tag == 'way':
        for i in way_attr_fields:
            way_attribs[i] = element.get(i)

        count = 0

        for x in element.iter('nd'):
            way_nodes_dict = {
                'id': way_attribs['id'],
                'node_id': x.get('ref'),
                'position': count
            }

            count += 1
            way_nodes.append(way_nodes_dict)

        for j in element.iter('tag'):
            key = j.get('k')
            val = j.get('v')

            # drop problematic tags
            if re.match(problem_chars, key):
                continue
            if key == 'addr:state' and val != 'TX':
                continue
            if key == 'addr:postcode':
                if filter_postcode(val):
                    continue
            if key == 'surface':
                if filter_surface(val):
                    continue

            # cleaning functions
            if key == 'addr:postcode':
                val = clean_postcode(val)
            elif key == 'addr:city':
                val = clean_city(val)
            elif key == 'building':
                val = clean_building(val)
            elif key == 'surface':
                val = clean_surface(val)

            mat = re.match(LOWER_COLON, key)

            if mat:
                key_split = re.split(':', key, maxsplit=1)

                way_tags_dict = {
                    'id': way_attribs['id'],
                    'key': key,
                    'value': val,
                    'type': key_split[0]
                }

            else:
                way_tags_dict = {
                    'id': way_attribs['id'],
                    'key': key,
                    'value': val,
                    'type': default_tag_type
                }

            tags.append(way_tags_dict)

        return {
            'way': way_attribs,
            'way_nodes': way_nodes,
            'way_tags': tags
        }


# ========================================================================= #
#                   Assistant to the Regional Functions                     #
# ========================================================================= #

def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = eT.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)

    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, csv_schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""

    if validator.validate(element, csv_schema) is not True:
        field, errors = next(iter(validator.errors.items()))
        message_string = '''\nElement of type '{0}' has the following 
                            errors:\n{1}'''
        error_string = pprint.pformat(errors)

        raise Exception(message_string.format(field, error_string))


class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow(row)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# ========================================================================= #
#                           Main Function                                   #
# ========================================================================= #

def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'w', encoding='utf8') as nodes_file, \
            codecs.open(NODE_TAGS_PATH, 'w', encoding='utf8') as nodes_tags_file, \
            codecs.open(WAYS_PATH, 'w', encoding='utf8') as ways_file, \
            codecs.open(WAY_NODES_PATH, 'w', encoding='utf8') as way_nodes_file, \
            codecs.open(WAY_TAGS_PATH, 'w', encoding='utf8') as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            elem = shape_element(element)

            if elem:
                if validate is True:
                    validate_element(elem, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(elem['node'])
                    node_tags_writer.writerows(elem['node_tags'])

                elif element.tag == 'way':
                    ways_writer.writerow(elem['way'])
                    way_nodes_writer.writerows(elem['way_nodes'])
                    way_tags_writer.writerows(elem['way_tags'])


# ========================================================================= #
#                               Execute                                     #
# ========================================================================= #

if __name__ == '__main__':
    py = os.path.basename(__file__)
    print('\nExecuting ' + py + '....')
    t.tic()

    process_map(OSM_PATH, validate=False)

    t.toc()





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''