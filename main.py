import random
import sys

def guess_number(chances, computer_choice):
    attempts = 0
    for i in range(chances):
        
        print("Enter your guess: ")
        guess = int(input())
        attempts += 1
        if computer_choice == guess:
            print(f"congratulations! You guessed the correct number in {attempts} attempts")
            sys.exit()
        elif computer_choice > guess:
            print(f"Incorrect. The number is greater than {guess}")
        elif computer_choice < guess:
            print(f"Incorrect. The number is less than {guess}")
        else:
            continue
           

print("***********************************")
print("welcome to my Number Guessing Game!\n", "I'm thinking of a number between 1 and 100.")
print()

print("Please select the difficulty level:\n", "1. Easy (10 chances)\n", "2. Medium (5 chances)\n", "3. Hard (3 chances)")
difficulty = input("")

if (difficulty == "1"):
    chances = 10
elif (difficulty == "2"):
    chances = 5
elif (difficulty == "3"):
    chances = 3
else:
    sys.exit()

computer_choice = random.randint(1, 100)

guess_number(chances, computer_choice)
