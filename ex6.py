def answernotvalid(): #answernotvalid is defined so if the user types anything that is not "yes" or "no" it will execute the print statement and the program will return to the beginning looking for a valid answer 
    answer = input("Invalid syntax, please type Yes or No: ")
    while answer != ("yes", "no"):
        answernotvalid()
    if answer == ("yes"):
         main()
    if answer == ("no"):
        exit()


def start(): 
    
    answer = input("Hi do you have a minute? ").lower()
    if answer == ("yes"):
        print("Great lets get started! ")
        main()
    if answer == ("no"):
        print("I'm sorry to hear that, maybe next time! ")
        exit()
    if answer == ("yes" , "no"):
        answernotvalid()

def main():
    name = input("What is your name? ")
    print(f"Hi there {name} nice to meet you")

    age = int(input("How old are you if you dont mind me asking? "))

    if(age < 18):
        print(f"Ahh im sorry, our minimum age for this site is 18! Please come back in {18-age} years!")
    else:
        print(f"You are {age} years old")

    height = float(input("How tall are you in inches? "))
    print(f"You are {height} inches tall. Which is {height*2.54} in centimetres or {height/12} feet if you were interested")

    weight = float(input("What is your weight in kilograms? "))
    print(f"You weigh {weight} Kilograms. Which is {weight*2.205} pounds if you were interested!")

    eye_colour = input("What colour are you eyes? ")
    hair_colour = input("What colour is your hair? ")

    print(f"Thanks for the info {name}. You are {age} years old, {height} inches tall, your total weight (according to you) is {weight} kg , the colour of your eyes are {eye_colour} and your hair is {hair_colour}")

start()
answernotvalid()
main()
