beer = 99

while (beer > 0):
    print(f"{beer} bottles of beer on the wall, {beer} bottles of beer. ")
    beer = beer -1    
    print(f"take one down, pass it around, {beer} bottles of beer on the wall...")
#if (beer == 2):
      #print(f"take one down, pass it around, {beer} bottle of beer on the wall")
if (beer == 1):
      print(f"{beer} bottle of beer on the wall, {beer} bottle of beer. ")
else:
    print(f"No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {beer} bottles of beer on the wall...")
