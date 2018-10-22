beer = 99

while (beer > 0):
    print(str(beer)+" bottles of beer on the wall," +
          str(beer) + " bottles of beer. ")
    beer = beer -1
    print("take one down, pass it around," +
          str(beer)+" bottles of beer on the wall...")

else:
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more," +
          str(beer) + "bottles of beer on the wall...")
