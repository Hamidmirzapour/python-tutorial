""""
This module practice working with tuple data structure.
Tuples are like Lists, just tuples are immutable.
"""

courses = ("Math", "History", "Art")
nums = (5, 2, 10, 7, 3, 8, 23)

print(courses)
print(len(courses))

# Indexing
print(courses[0])
print(courses[-1])

# Slicing
print(courses[:2])
print(courses[-1:1:-1])
print(courses[::-1])

# Some methods of tuple obj
print(courses.index("Art"))
print(courses.count("Art"))

sorted_courses = sorted(courses)
print(sorted_courses)

# Tuples are immutable: can not be modified
list_1 = ("Test 1", "Test 2", "Test 3")
list_2 = list_1
print(list_1)
print(list_2)

# list_1[0] = "Test One"
# TypeError: 'tuple' object does not support item assignment

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()