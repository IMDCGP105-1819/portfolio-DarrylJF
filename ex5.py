beerBottles = 99
story = (f"{beerBottles} bottles of beer on the wall, {beerBottles} bottles of beer.\nTake one down, pass it around, {beerBottles} bottles of beer on the wall")

while (beerBottles >= 1):
    if beerBottles != 0:
        print(story)
        beerBottles = beerBottles - 1
    else:
        print("You made it!")
        break
