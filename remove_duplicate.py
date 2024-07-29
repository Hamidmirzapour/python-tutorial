numbers = [12, 5, 8, 12, 8, 10, 10, 10, 10, 27, 50]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
