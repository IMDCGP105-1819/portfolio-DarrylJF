answer = input(
    "Hi there, If you have a moment i'd like to ask you a few questions is that ok? Type Yes or No:" + " ")

if(answer) == "no":
    print("I'm sorry to hear that!!")
if(answer) == "yes":
    print("Great! Lets get started!")
name = input("What is your name?" + " ")
print("Hi there" + " " + str(name) + " " + "nice to meet you")
age = int(input("How old are you if you dont mind me asking?" + " "))
if(age <= 18):
    print("Ahh im sorry, our minimum age for this site is 18! Please come back in" +
          " " + str(18-age) + " " + "years!")
