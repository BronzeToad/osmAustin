# ========================================================================= #
#   WGU - Udacity: Data Wrangling
#   OpenStreetMap - ATX
#   Functions for building tag
# ========================================================================= #

building_dict = {
    'Bing': 'yes',
    'Learning_Center/_Day_Care': 'learning_center',
    'sports_centre': 'sports_center'
}


def clean_building(val):
    """Cleans key values for building tag"""

    # compare val to dictionary - if val in dict keys, replace with dict value
    for key in building_dict.keys():
        if val == key:
            val = building_dict.get(key)

    # replace any space with underscore
    val = val.replace(' ', '_')

    return val





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''