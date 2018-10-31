
from random import randint

guess = int(input())
guesses = 0



def random_number(low,high):
    return randint
print("Enter your guess from numbers 1 to 100: ")
guess = int(input())
guesses = 0

while guess != random_number:
    if guess < random_number:
        print("Higher")
    elif guess > random_number:
        print("Lower")
    else:
        print("You got it! It took you ", guesses + "guesse/s")
    guesses+=1

random_number(1,100)