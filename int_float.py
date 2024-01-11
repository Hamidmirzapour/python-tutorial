"""
This module practice working with integer and float data type
"""
# Arithmetic Operators:
# Addition:            3 + 2
# Subtraction:         3 - 2
# Multiplication:      3 * 2
# Division:            3 / 2
# Floor Division:      3 // 2
# Exponent:            3 ** 2
# Modolus:             3 % 2

# Comparisons:
# Equal:               3 == 2
# Not Equal:           3 != 2
# Greater Than         3 > 2
# Less Than            3 < 2
# Greater or Equal:    3 >= 2
# Less or Equal:       3 <= 2

number_1 = 3
number_2 = 2
number_3 = 2.6

print(type(number_1), type(number_3))
print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)
print(number_1 // number_2)
print(number_1 ** number_2)
print(number_1 % number_2)

# Increment and Decrement
number_1 += 1
print(number_1)

number_1 -= 1
print(number_1)

print(3 == 2)
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)

# Some functions on numbers
print(abs(-10))
print(round(2.755))
print(round(2.755, 1))

# Type Casting: Cast from string to int and float
num_1 = '1245'
num_2 = '36.5'
print(num_1 + num_2) # Concatenate two string
print(int(num_1) + float(num_2)) # Casting and Summation