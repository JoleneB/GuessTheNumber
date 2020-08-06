import random
num = random.randrange(1,100)
guess = int(input("Guess a number between 1 and 50: "))

def tryAgain():

    while guess != num:

        try:
            if guess < num:
                print("You need to guess higher. Try again")
                guess = int(input("Guess a number between 1 and 50: "))

            elif guess < 1 or guess > 100:
                print("Sorry, you must choose a number between 1 and 50")
                guess = int(input("Guess a number between 1 and 50: "))

            elif guess > num:
                print("You need to guess lower. Try again")
                guess = int(input("Guess a number between 1 and 50: "))

            print("\nWoo you guessed the number correctly! :)")

        except ValueError:
            raise ValueError("please enter a digit")
            tryAgain()
            break
tryAgain()








