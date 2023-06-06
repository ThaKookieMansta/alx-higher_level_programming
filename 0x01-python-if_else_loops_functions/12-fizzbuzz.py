#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            j = "FizzBuzz"
        elif i % 3 == 0:
            j = "Fizz"
        elif i % 5 == 0:
            j = "Buzz"
        else:
            j = i
        print(j, end=" ")
