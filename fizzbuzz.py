def fizz_thing(n):
    for i in range(0,n+1):
        if (i % 3) == 0 and (i % 5) != 0:
            print("Fizz")
        elif (i % 5) == 0 and (i % 3) != 0:
            print("Buzz")
        elif (i % 5) == 0 and (i % 3) == 0:
            print("FizzBuzz")
        else:
            print (i)
fizz_thing(100)