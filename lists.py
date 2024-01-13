""""
This module practice working with list data structure
"""

courses = ["Math", "History", "Art"]
nums = [5, 2, 10, 7, 3, 8, 23]

print(courses)
print(len(courses))

# Indexing
print(courses[0])
print(courses[-1])

# Slicing
print(courses[:2])
print(courses[-1:1:-1])
print(courses[::-1])

# Some methods of list obj
courses.append("Algorithm Design")
print(courses)

courses.insert(0, "Compiler Design")
print(courses)

courses.extend(["Computer Architecture", "Engineering Math"])
print(courses)

courses.remove("Compiler Design")
print(courses)

popped = courses.pop()
print(courses)
print(popped)

print(courses.index("History"))

courses.sort()
nums.sort(reverse=True)
print(courses)
print(nums)

sorted_courses = sorted(courses)
print(sorted_courses)

# Lists are mutable: can be modified
list_1 = ["Test 1", "Test 2", "Test 3"]
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = "Test One"
print(list_1)
print(list_2)

# Empty list
empty_list = []
empty_list = list()