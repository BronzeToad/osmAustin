# ========================================================================= #
#   WGU - Udacity: Data Wrangling
#   OpenStreetMap - ATX
#   Functions for addr:postcode tag
# ========================================================================= #

atx_postcodes = [
    '78610', '78613', '78617', '78641', '78652', '78653', '78660', '78664',
    '78681', '78701', '78702', '78703', '78704', '78705', '78712', '78717',
    '78719', '78721', '78722', '78723', '78724', '78725', '78726', '78727',
    '78728', '78729', '78730', '78731', '78732', '78733', '78734', '78735',
    '78736', '78737', '78738', '78739', '78741', '78742', '78744', '78745',
    '78746', '78747', '78748', '78749', '78750', '78751', '78752', '78753',
    '78754', '78756', '78757', '78758', '78759'
]


def filter_postcode(val):
    """Filters key values for addr:postcode tag"""

    # run val through postcode cleaning function
    val = clean_postcode(val)

    # set to true if val is not an austin, tx zip code
    if val not in atx_postcodes:
        return True
    else:
        return False


def clean_postcode(val):
    """Cleans key values for addr:postcode tag"""

    # remove multiple zip code entries (e.g. '12345; 98765')
    split_val = val.split(';', maxsplit=1)
    val = split_val[0]

    # drop last four from full zip codes (e.g. 12345-6789 -> 12345)
    if len(val) == 10:
        val = val[0:5]

    return val





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''