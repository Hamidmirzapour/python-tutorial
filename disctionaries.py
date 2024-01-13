""""
This module practice working with dictionary data structure.
"""

student = {"name": "John", "age": 25, "courses": ["Math", "Physics"]}

print(student)
print(student["name"])
print(student.get("name"))
print(student.get("Phone"))
print(student.get("Phone", "Not Found"))

student["phone"] = "555-5555"
print(student)


# Some functions and methods of dictionary obj
student.update({"name": "Joe", "age": 30, "gender": "Male"})
print(student)

del student["age"]
print(student)

gender = student.pop("gender")
print(student)
print(gender)

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(f"{key}: {value}")