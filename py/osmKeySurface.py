# ========================================================================= #
#   WGU - Udacity: Data Wrangling
#   OpenStreetMap - ATX
#   Functions for surface tag
# ========================================================================= #

surface_dict = {
    'con': 'concrete',
    'large,_unattached_stones_through_water': 'stones',
    'Large_unattached_stones_laid_in_the_creek': 'stones',
    'paving_stones:30': 'paving_stones',
    'creekbed_(rock)': 'rock',
    'concrete,_dirt': 'concrete;dirt',
    'dirt/sand': 'dirt;sand',
    'concrete:lanes': 'concrete',
    'concrete:plates': 'concrete'
}

remove_list = [
    'yes', 'CR_127', 'f'
]


def filter_surface(val):
    """Cleans key values for surface tag"""

    # set to true if val is on the remove list
    if val in remove_list:
        return True
    else:
        return False


def clean_surface(val):
    """Cleans key values for surface tag"""

    # compare val to dictionary - if val in dict keys, replace with dict value
    for key in surface_dict.keys():
        if val == key:
            val = surface_dict.get(key)

    return val





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''