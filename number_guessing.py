from random import randint

low_num, high_num = 1, 10
random_number: int = randint(low_num, high_num)
print(f"Guess the number in the range from {low_num} to {high_num}.")

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError as e:
        print("Enter a valid number.")
        continue

    if guess > random_number:
        print("The number is lower")
    elif guess < random_number:
        print("The number is higher")
    else:
        print("Guessed it!")
        break