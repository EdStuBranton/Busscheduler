import time
import datetime

__author__ = "Ed Stu Branton"
__copyright__ = "Copyright 2020 Ed Stu Branton"
__credits__ = ["Ed Stu Branton"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ed Stu Branton"
__email__ = "edstubranton@hotmail.com"
__status__ = "Production"


# '''#Notes
# -Tasks
# include a function that takes the average walking speed of a human and calculates the time needed to get to the next bus station
# Make a function that finds the next two available busses at the current hour from the schedule
# 
# '''

"""
Busschedule input as Dictionary
"""

schedule_search_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

busschedule_weekday = {'a':[8,25], 'b':[8,45],
        'c':[9,25], 'd':[9,45],
        'e':[10,25], 'f':[10,45],
        'g':[11,25], 'h':[11,45],
        'i':[12,25], 'j':[12,45],
        'k':[13,25], 'l':[13,45],
        'm':[14,25], 'n':[14,45],
        'o':[15,25], 'p':[15,45],
        'q':[16,25], 'r':[16,45],
        's':[17,25], 't':[17,45],
        'u':[18,25], 'v':[18,45]}

def calc_time_diff(lst1, lst2):
    c = [a - b for a, b in zip(lst1, lst2)]
    if c[0] < 0:
        c[0] += 24
    if c[1] < 0:
        c[1] += 60
    return c

def rtrn_curr_hr_min_split():    
    return [int(value) for value in time.strftime("%H:%M").split(':')]

def normalize_hours(remaining_hours):
    if remaining_hours < 0:
        remaining_hours += 24    
    return remaining_hours

def normalize_minutes(remaining_minutes):
    if remaining_minutes < 0:
        remaining_minutes += 60        
    return remaining_minutes

def time_needed_to_busstation(m):
    result = int((((m / 1000) / 5) * 3600))
    minutes = int(result / 60)
    seconds = result - (minutes * 60) 
    
    return '{0} Minute/s and {1} Second/s'.format(minutes, seconds)

def return_schedule():
    return [calc_time_diff(busschedule_weekday[key], rtrn_curr_hr_min_split()) for key in schedule_search_index]

def return_next_bus():
    hours, minutes = min(return_schedule())
    return 'The next bus will arrive in {0} hours and {1} minutes'.format(penis, vagina)


print(return_next_bus())
