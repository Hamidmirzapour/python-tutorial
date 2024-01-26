""""
This module practice working with comprehensions.
list comprehension, tuple comprehension, dictionary comprehension, set comprehension, lambda, map, filter, generator comprehension
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each n in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# List Comprehension method
my_list = [n for n in nums]
print(my_list)

# ------------------------------------------------------------------------------------------------#

# I want 'n * n' for each n in nums
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

# List Comprehension method
my_list = [n * n for n in nums]
print(my_list)

# map + lambda method
my_list = list(map(lambda n: n * n, nums))
print(my_list)

# ------------------------------------------------------------------------------------------------#

# I want 'n' for each n in nums if n is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# List Comprehension method
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# filter + lambda method
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list)

# ------------------------------------------------------------------------------------------------#

# I want (letter, num) pair for each letter in 'a,b,c,d' and each num in 1,2,3,4
my_list = []
for letter in 'abcd':
    for num in [1,2,3,4]:
        my_list.append((letter, num))
print(my_list)

# List Comprehension method
my_list = [(letter, num) for letter in 'abcd' for num in [1,2,3,4]]
print(my_list)

# ------------------------------------------------------------------------------------------------#

first_name = ["Hamid", "Ehsan", "Shahryar", "Mina"]
last_name = ["Mirzapour", "Paydar", "Shafiee", "Dinari"]
print(list(zip(first_name, last_name)))

my_dict = {}
for f, l in zip(first_name, last_name):
    my_dict[f] = l
print(my_dict)

# Dictionary Comprehension method
my_dict = {f: l for f, l in zip(first_name, last_name)}
print(my_dict)

# Dictionary Comprehension method for name is not hamid
my_dict = {f: l for f, l in zip(first_name, last_name) if f != "Hamid"}
print(my_dict)

# ------------------------------------------------------------------------------------------------#

num_set = {1,1,1,2,2,3,3,5,6,6,8,9,9,9,10}
my_set = set()
for num in num_set:
    my_set.add(num)
print(my_set)

# Set Comprehension
my_set = {n for n in num_set}
print(my_set)

# ------------------------------------------------------------------------------------------------#

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generator Expression
# I want yield 'n * n' for each n in nums
def gen_func(nums):
    for n in nums:
        yield n * n

my_gen = gen_func(nums)
print(my_gen)

# Generator Comprehension
my_gen = (n * n for n in nums)
print(my_gen)
# ------------------------------------------------------------------------------------------------#
