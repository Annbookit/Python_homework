
def fizz_bizz (n):
    for x in range (1, n):
        if (x % 3 == 0):
            print("Fizz")
        elif (x % 5 == 0):
            print("Buzz")
        elif (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")
        else:
            print(x)



fizz_bizz (17)




