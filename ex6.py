answer = input(
    "Hi there, If you have a moment i'd like to ask you a few questions is that ok? Type Yes or No:" + " ")

if(answer) == "no":
    print("I'm sorry to hear that!!")
if(answer) == "yes":
    print("Ok! Lets get started!")

name = input("What is your name?" + " ")
print("Hi there" + " " + str(name) + " " + "nice to meet you")

age = int(input("How old are you if you dont mind me asking?" + " "))
if(age <= 18):
    print("Ahh im sorry, our minimum age for this site is 18! Please come back in" +
          " " + str(18-age) + " " + "years!")
else:
    print("You are" + " " + str(age) + " " + "years old")

height = float(input("How tall are you in inches?" + " "))
print("You are" + " " + str(height) + " " + "inches tall. Which is" + " " +
      str(height*2.54) + " " + "in centimetre's or" + " " + str(height/12) + " " + "feet if you were interested :)")

weight = float(input("What is your weight in kilograms?" + " "))
print("You weigh" + " " + str(weight) + " " + "Kilograms. Which is" +
      " " + str(weight*2.205) + " " + "pounds incase you were interested!")
