count = 0

while count < 100:
    if count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    elif count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    else:
        print(count)
    count += 1
