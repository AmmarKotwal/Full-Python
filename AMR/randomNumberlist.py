import random as rd
import sys

print("*** Random Number Guessing Game ****\n")
computer_number = rd.randint(1, 20)
lives = 3

while lives > 0:
    try:
        user_input = int(input("Enter Any Number between 1 - 20: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if user_input == computer_number:
        print("Congratulations You've Guessed!!")
        sys.exit()

    lives -= 1

    if user_input > computer_number:
        print("* Hint : Think Lower Number")
    elif user_input < computer_number:
        print("* Hint : Think Higher Number")

    if lives == 0:
        print("Lives Ended. Game Over!")
        print(f"The correct number was {computer_number}.")
    else:
        print(f"{lives} Remaining")