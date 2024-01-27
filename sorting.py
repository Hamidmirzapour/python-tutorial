""""
This module practice working with sorting lists, tuples, dictionaries
"""

nums = [5, 3, 6, 2, 1, 7, 8, 12, 10]
sorted_nums = sorted(nums)

print(f"Sorted Nums: {sorted_nums}")
print(f"Original Nums: {nums}")


nums = (5, 3, 6, 2, 1, 7, 8, 12, 10)
sorted_nums = sorted(nums)

print(f"Sorted Nums: {sorted_nums}")
print(f"Original Nums: {nums}")

persons = {"name": ["Ali", "Zahra", "Hamid"], "age": [30, 25, 28]}
sorted_persons = sorted(persons)

print(f"Sorted Persons: {sorted_persons}") # Sort Keys
print(f"Original Persons: {persons}")

sorted_persons = sorted(persons.items())
print(f"Sorted Persons: {sorted_persons}") # Sort based on keys
print(f"Original Persons: {persons}")

