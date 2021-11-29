# ========================================================================= #
#   WGU - Udacity: Data Wrangling
#   OpenStreetMap - ATX
#   Create table of sizes for project files
# ========================================================================= #

import os
import pandas as pd
from TicToc import TicToc
t = TicToc()

# ========================================================================= #
#                           Define Variables                                #
# ========================================================================= #

root_data = '/Users/ajp/dsProjects/workspace/osmAustin/data/'
root_csv = root_data + 'csv/'

osm = 'austin_texas.osm'
sample = 'sample_atx.osm'
nodes_tags = 'nodes_tags.csv'
nodes = 'nodes.csv'
ways_nodes = 'ways_nodes.csv'
ways_tags = 'ways_tags.csv'
ways = 'ways.csv'

path_osm = root_data + osm
path_sample = root_data + sample
path_nodes_tags = root_csv + nodes_tags
path_nodes = root_csv + nodes
path_ways_nodes = root_csv + ways_nodes
path_ways_tags = root_csv + ways_tags
path_ways = root_csv + ways

# ========================================================================= #
#                             Size Function                                 #
# ========================================================================= #


def get_size(filepath):
    """Get file size and return string with appropriate unit"""

    size_bytes = os.path.getsize(filepath)

    if size_bytes < 1024:
        size_bytes = round(size_bytes, 2)
        size = f'{size_bytes} B'
    else:
        size_kilobytes = size_bytes / 1024
        if size_kilobytes < 1024:
            size_kilobytes = round(size_kilobytes, 2)
            size = f'{size_kilobytes} KB'
        else:
            size_megabytes = size_kilobytes / 1024
            if size_megabytes < 1024:
                size_megabytes = round(size_megabytes, 2)
                size = f'{size_megabytes} MB'
            else:
                size_gigabytes = size_megabytes / 1024
                if size_gigabytes < 1024:
                    size_gigabytes = round(size_gigabytes, 2)
                    size = f'{size_gigabytes} GB'
                else:
                    size = "Wow, that's huge."

    return size


# ========================================================================= #
#                               Execute                                     #
# ========================================================================= #

if __name__ == '__main__':
    py = os.path.basename(__file__)
    print('\nExecuting ' + py + '....')
    t.tic()

    osm_size = get_size(path_osm)
    sample_size = get_size(path_sample)
    nodes_tags_size = get_size(path_nodes_tags)
    nodes_size = get_size(path_nodes)
    ways_nodes_size = get_size(path_ways_nodes)
    ways_tags_size = get_size(path_ways_tags)
    ways_size = get_size(path_ways)

    names = [
        osm,
        sample,
        nodes_tags,
        nodes,
        ways_nodes,
        ways_tags,
        ways
    ]

    sizes = [
        osm_size,
        sample_size,
        nodes_tags_size,
        nodes_size,
        ways_nodes_size,
        ways_tags_size,
        ways_size
    ]

    sizes_dict = {
        'name': names,
        'size': sizes
    }

    sizes_df = pd.DataFrame(data=sizes_dict)
    print(sizes_df)

    t.toc()





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''