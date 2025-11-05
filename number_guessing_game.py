# This is a number-guessing game. The computer randomly chooses a number between 1 and 100. 
# It tells you whether your guess is too low or too high helping you find the correct number.

import random

number = round(random.randint(1, 100))

print("This is a number-guessing game.\n")
guess = 0
steps = 1

while guess != number:

    try:
        guess = int(input("Please type a number between 1 and 100.\n"))
        if guess not in range(1, 100):
            print("\nInvalid value given.")
        elif number > guess:
            print("\nYour guess is too low.")
        elif number < guess:
            print("\nYour guess is too high.")

        else:
            print(f"\nYou have found it in {steps} steps. Well done! :)")
        steps += 1

    except ValueError:
        print("\nThis is not a number.\n")
