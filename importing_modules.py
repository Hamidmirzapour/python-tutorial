""""
This module practice working with importing mudules.
"""

# import my_module
# import my_module as mm
from my_module import find_index, test

# Some python standard libraries
import os
import sys
import random
import math
import datetime
import calendar

courses = ["Math", "Art", "CompSci", "Science", "History"]

# index = my_module.find_index(courses, "CompSci")
# index = mm.find_index(courses, "CompSci")
index = find_index(courses, "CompSci")
print(index)
print(test)

# Get a random item from a list
random_course = random.choice(courses)
print(random_course)

# Calculate sin of 90 degree
rads = math.radians(90)
sinus = math.sin(rads)
print(sinus)

# Get date of today
print(datetime.date.today())

# Leap year
print(calendar.isleap(2024))

# Show current directory
print(os.getcwd())

# Show the directory that library is there
print(os.__file__)


# Show all paths to search for modules
# print(sys.path)

# Add a path of my_modules is in my Desktop
# sys.path.append("C://Users/Hamid/Destop/my_modules")

