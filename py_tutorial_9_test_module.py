import sys  # to find module path

# sys.path.append('/users/........./Files')   # adding module locationg manually
# not a good approach

#creating a new environmental variable
# system properties > Environmental variables > Variable Name: PYTHONPATH  Variable Value: add location
#cmd > python > import my_module (to check)



# import py_tutorial_9_my_modules as mm

# from py_tutorial_9_my_modules import find_index

from py_tutorial_9_my_modules import find_index, test

# from py_tutorial_9_my_modules import *    # this is not good



list = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(list, 'Math')

index = find_index(list, 'Math')      # we have only access to index funciton
# print(index)
# print(test)


# print(sys.path)



# importing standard library

import random

random_choice = random.choice(list)

print(random_choice)


import math

rads = math.radians(90)  # degree to radian convension
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2024))

import os       # access to underlying operating system

print(os.getcwd())
# this library can use to create file delete file and so on

print(os.__file__)

