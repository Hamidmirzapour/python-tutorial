from random import randint

def roll_dice(amount: int) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        rolls.append(randint(1, 6))

    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many rolls would you like? ")
            if user_input.lower() == "exit":
                print("Thanks for playing!")
                break
            print(*roll_dice(int(user_input)), sep=", ")
        except ValueError as e:
            print("(Enter a valid number!)")

if __name__ == "__main__":
    main()