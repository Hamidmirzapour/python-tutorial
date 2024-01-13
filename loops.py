""""
This module practice working with loops.
while, for, in, range, break, continue
"""

students = ["Ali", "Akbar", "Hamid", "Mary", "Zahra", "Mina"]

# For Loop
for student in students:
    print(student)

print("\n")

for student in students:
    if student == "Hamid":
        print("Found!")
        break
    print(student)

print("\n")

for student in students:
    if student == "Hamid":
        print("Found!")
        continue
    print(student)

print("\n")

for i in range(10):
    print(i)

print("\n")

for i in range(1, 11, 2):
    print(i)

print("\n")


# While Loop
count = 0
while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1