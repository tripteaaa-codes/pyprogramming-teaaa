import random 

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess < number:
        print("Too low! try again")

    elif guess > number:
        print("Too high! Try again")

    else:
         print("congrats to guess the correct number")