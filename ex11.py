from random import randint

low = 0
high = 100
guesses=0
number = randint(low,high)
guess = input()

def random_number():
    int(input("Guess a number between 1 and 100: "))
while guess != number:
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print("You got it! It took you", guesses, "guesse/s...")
    guesses+=1
    
random_number()