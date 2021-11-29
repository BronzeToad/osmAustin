# ========================================================================= #
#   WGU - Udacity: Data Wrangling
#   OpenStreetMap - ATX
#   Functions for audit notebook
# ========================================================================= #

import xml.etree.ElementTree as eT
import os
from TicToc import TicToc
t = TicToc()

# ========================================================================= #
#                           Define Variables                                #
# ========================================================================= #

wd = '/Users/ajp/dsProjects/workspace/osmAustin/data/'
atx_filename = wd + 'austin_texas.osm'
# atx_filename = wd + 'sample_atx.osm'
# atx_filename = wd + 'small_sample_atx.osm'

# ========================================================================= #
#                              Functions                                    #
# ========================================================================= #


def print_sorted_dict(d, sort_by=None):
    """Prints dictionary sorted by keys or items"""

    if sort_by is None:
        sort_by = 'items'

    if sort_by == 'keys':
        sorted_dict = sorted(d.keys(), key=lambda s: s.lower())
    elif sort_by == 'items':
        sorted_dict = dict(sorted(d.items(), key=lambda s: s[1], reverse=True))
    else:
        print("Invalid sort_by: please input 'keys' or 'items'\n")
        sorted_dict = d

    for k in sorted_dict:
        v = d[k]
        print(f'{k}: {v}')


def count_elements(filename):
    """Prints element tag name and count for each XML element."""

    d = {}

    for event, elem in eT.iterparse(filename, events=('start',)):
        if elem.tag not in d:
            d[elem.tag] = 1
        else:
            d[elem.tag] += 1

    print('\n----- Count all tags -----')
    print_sorted_dict(d)
    return


def count_attributes(filename):
    """Prints attribute name and count for each XML element."""

    d = {}

    for event, elem in eT.iterparse(filename, events=('start', 'end')):
        if event == 'end':
            for attr in elem.attrib:
                if attr not in d:
                    d[attr] = 1
                else:
                    d[attr] += 1

    print('\n----- Count all attributes -----')
    print_sorted_dict(d)


def count_keys(filename):
    """Prints key name and count for each XML element."""

    d = {}

    for event, elem in eT.iterparse(filename, events=('start', 'end')):
        if event == 'end':
            key = elem.attrib.get('k')
            if key:
                if key not in d:
                    d[key] = 1
                else:
                    d[key] += 1

    print('\n----- Count all keys -----')
    print_sorted_dict(d)


def key_val_counter(filename, key_name):
    """Prints key name and count for each instance of key_name"""

    d = {}

    for event, elem in eT.iterparse(filename, events=('start', 'end')):
        if event == 'end':
            key = elem.attrib.get('k')
            if key == key_name:
                val = elem.attrib.get('v')
                if val not in d:
                    d[val] = 1
                else:
                    d[val] += 1

    print('\n----- Count of values for key: ' + key_name + ' -----')
    print_sorted_dict(d)


# ========================================================================= #
#                               Execute                                     #
# ========================================================================= #

if __name__ == '__main__':
    py = os.path.basename(__file__)
    print('\nExecuting ' + py + '....')
    t.tic()

    # get count of elements
    count_elements(atx_filename)

    # get count of attributes
    count_attributes(atx_filename)

    # get count of keys
    count_keys(atx_filename)

    # no cleaning needed
    key_val_counter(atx_filename, 'height')
    key_val_counter(atx_filename, 'addr:street')
    key_val_counter(atx_filename, 'addr:housenumber')
    key_val_counter(atx_filename, 'highway')
    key_val_counter(atx_filename, 'name')
    key_val_counter(atx_filename, 'service')
    key_val_counter(atx_filename, 'tiger:county')

    # some cleaning required
    key_val_counter(atx_filename, 'building')
    key_val_counter(atx_filename, 'addr:postcode')
    key_val_counter(atx_filename, 'surface')
    key_val_counter(atx_filename, 'addr:city')
    key_val_counter(atx_filename, 'addr:state')

    t.toc()





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''