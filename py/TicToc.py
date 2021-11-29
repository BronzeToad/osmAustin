# ========================================================================= #
#                              TicToc - Timer                               #
# ========================================================================= #

import time
import math as m


class TicTocError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class TicToc:
    def __init__(self):
        self._start_time = None

    def tic(self):
        """Start a new timer"""
        # if self._start_time is not None:
        # raise TicTocError(f"Timer is running. Use .toc() to stop it")
        self._start_time = time.perf_counter()

    def toc(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TicTocError(f"Timer is not running. Use .tic() to start it")

        time_diff_seconds = round(time.perf_counter() - self._start_time, 4)
        self._start_time = None

        if time_diff_seconds > 3600:
            hour = m.floor(time_diff_seconds // 3600)
            time_diff_seconds = m.floor(time_diff_seconds % 3600)
            min = m.floor(time_diff_seconds // 60)
            sec = m.floor(time_diff_seconds % 60)
            print(f'\n--- Elapsed time: {hour} hours, {min} minutes, and {sec} seconds ---')

        elif time_diff_seconds > 60:
            min = m.floor(time_diff_seconds) // 60
            sec = m.floor(time_diff_seconds) % 60
            print(f'\n--- Elapsed time: {min} minutes and {sec} seconds ---')

        else:
            sec = m.floor(time_diff_seconds)
            print(f'\n--- Elapsed time: {sec} seconds ---')





''' ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  / 
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /  
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/ '''