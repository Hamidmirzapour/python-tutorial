""""
This module practice working with conditionals.
if, elif, else
"""
# Comparisons:
# Equal:               3 == 2
# Not Equal:           3 != 2
# Greater Than         3 > 2
# Less Than            3 < 2
# Greater or Equal:    3 >= 2
# Less or Equal:       3 <= 2
# is:         Object Identity

# Logical Operators:
# and
# or
# not

language = "JavaScript"

if language == "Python":
    print("This is Python Language.")
elif language == "Java":
    print("This is Java Language.")
elif language == "JavaScript":
    print("This is JavaScript Language.")
else:
    print("No Match.")    


user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin page")
elif user == "User" and logged_in:
    print("User Dashboard")
elif not logged_in:
    print("Please login")
else:
    print("Welcome")


a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))

c = [1, 2, 3]
d = c
print(c == d)
print(c is d)
print(id(c))
print(id(d))


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), []
    # Any empty mapping. For example, {}

print(False == True)
print(None == True)
print(0 == True)
print('' == True)
print(() == True)
print([] == True)
print({} == True)