print("Addition\nSubtraction\nMultiplication\nDevision")
try:
    first_number = int(input("First Number: "))
    operator = input("Operator: ").lower()
    second_number = int(input("Second Number: "))
    result = 0
    if operator == "addition":
        result = first_number + second_number
    elif operator == "subtraction":
        result = first_number - second_number
    elif operator == "multiplication":
        result = first_number * second_number
    elif operator == "devision":
        result = first_number / second_number
    else:
        print("Sorry I don't understand your operator!!!")
    print(result)
except ValueError as e:
    print("Invalid input.")
except ZeroDivisionError:
    print("For Devision Second number must be non-zero number.")
