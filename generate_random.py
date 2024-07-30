import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 1000))

players = ["Bob", "Sara", "Hamid", "Zahra", "David"]
leader = random.choice(players)
print(f"Leader: {leader}")