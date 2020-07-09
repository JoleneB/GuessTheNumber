import random

num = random.randrange(1,50)
guess = int(input("Guess a number between 1 and 50: "))


while guess != num:
    try:
        if guess < num:
            print("You need to guess higher. Try again")
            guess = int(input("Guess a number between 1 and 50: "))

        elif guess < 1 or guess > 50:
            print("Sorry, you must choose a number between 1 and 50")
            guess = int(input("Guess a number between 1 and 50: "))

        else:
            print("You need to guess lower. Try again")
            guess = int(input("Guess a number between 1 and 50: "))

    except ValueError:
        raise SyntaxError("Sorry, please enter a number.")
        guess = int(input("Guess a number between 1 and 50: "))

print("\nWoo you guessed the number correctly! :)")


