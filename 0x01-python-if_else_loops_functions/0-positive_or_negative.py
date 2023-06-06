#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    answer = "is positive"
elif number == 0:
    answer = "is zero"
else:
    answer = "is negative"
print(number, answer)
