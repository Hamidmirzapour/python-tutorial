""""
This module practice working with functions.
"""

def hello_world():
    print("Hello, World!")

def greeting(greeting, name="Hamid"):
    # print("{} {}".format(greeting, name))
    print(f"{greeting} {name}.")

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


def is_leap(year):
    """ Return True for leap years, False for non-leap years. """
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

hello_world()

greeting("Hello")
greeting("Hello", "John")

student_info("Math", "Art", name="John", age=25)

courses = ["Physics", "Chemistry"]
student = {"name": "Joe", "age": 30}
student_info(*courses, **student)

print(is_leap(2017))
print(is_leap(2020))