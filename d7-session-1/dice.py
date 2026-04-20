import random


def roll_dice(sides):
    return random.randint(1, sides)


print("--- Dice Simulator ---")

sides = int(input("How many sides on the dice? "))
num_dice = int(input("How many dice to roll? "))

again = "y"
while again == "y":
    total = 0
    for i in range(num_dice):
        result = roll_dice(sides)
        print(f"Dice {i + 1}: {result}")
        total += result
    print("Total:", total)
    again = input("Roll again? (y/n): ").lower()

print("Thanks for playing!")
