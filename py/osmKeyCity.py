# ========================================================================= #
#   WGU - Udacity: Data Wrangling
#   OpenStreetMap - ATX
#   Functions for addr:city
# ========================================================================= #

city_dict = {
    'Wells Branch': 'Austin',
    'Barton Creek': 'Austin',
    'Ste 128, Austin': 'Austin',
    'Pepe’s Tacos': 'Austin',
    'N Austin': 'Austin',
    'Austin;austin': 'Austin',
    'San Gabriel Village Boulevard': 'Georgetown',
    'Manchaca,': 'Manchaca',
    'Pfluggerville': 'Pflugerville'
}


def clean_city(val):
    """Cleans key values for addr:city tag"""

    # split multi-word city names
    split = val.split(' ')
    i = 0
    cap = ''

    # capitalize first letter of each word - put names back together
    while i < len(split):
        x = split[i].capitalize()
        if i == 0:
            cap = x
        else:
            cap = cap + ' ' + x
        i += 1

    val = cap

    # compare val to dictionary - if val in dict keys, replace with dict value
    for key in city_dict.keys():
        if val == key:
            val = city_dict.get(key)

    return val





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''