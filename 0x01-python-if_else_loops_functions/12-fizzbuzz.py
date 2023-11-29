#!/usr/bin/python3
def fizzbuzz():
    for d in range(1, 101):
        if d % 3 == 0 and d % 5 == 0:
            print("FizzBuzz ", end="")
        elif d % 3 == 0:
            print("Fizz ", end="")
        elif d % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(d), end="")
