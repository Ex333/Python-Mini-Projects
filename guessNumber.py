from random import randint
from art import text2art
from time import sleep

print(text2art("I wanna play a Game!"))

# Variables
number_to_guess = randint(1, 10)
tries = 3                  # how many tries user has
attempts = 0               # how many attempts user has made
guessed = -1

while guessed != number_to_guess and tries != 0:

    guessed = int(input("Guess the number!: 1-10!"))
    attempts += 1
    tries -= 1

    sleep(1)
    print("Calculating! . . .")
    sleep(2)
    print("Hacking NASA...")
    sleep(2)
    print("Receiving data...")
    sleep(2)
    print("Drinking coffee")
    sleep(1)

    if guessed > number_to_guess:
        print(f"Too high! Try one more time! You have {tries} tries left.")

    elif guessed < number_to_guess:
        print(f"Too low! Try one more time! You have {tries} tries left.")


if guessed == number_to_guess:
    print(
        f"Congrats! You guessed the number {number_to_guess} "
        f"in {attempts} attempts!!"
    )
else:
    print("Sorry! This game was too heavy for you. Maybe next time you will do it!")
    sleep(2)
    print("Sending your data to Cloud...")
    sleep(2)
    print("Selling your data...")