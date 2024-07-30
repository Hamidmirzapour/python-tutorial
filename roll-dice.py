import random

class Dice:

    def roll(self):
        self.first_number = random.randint(1, 7)
        self.second_number = random.randint(1, 7)
        return (self.first_number, self.second_number)
    
dice1 = Dice()
print(dice1.roll())