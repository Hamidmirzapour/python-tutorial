""""
This module practice working with set data structure.
Sets are unordered and doesn't allow duplicate items.
"""

courses = {"Art", "Math", "History", "Art"}
print(courses)

math_courses = {"Math", "Physics", "Literature", "Discrete Math", "Differential"}
science_courses = {"Math", "Physics", "Literature", "Chemistry", "Biology"}

print(math_courses.intersection(science_courses))
print(math_courses & science_courses)

print(math_courses.union(science_courses))
print(math_courses | science_courses)

print(math_courses.difference(science_courses))
print(math_courses - science_courses)

# Empty set
# empty_set = {} # Not working. it's used for empty dictionary
empty_set = set()