#!/usr/bin/python3
from sys import argv

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    no_of_arguments = len(argv) - 1
    if no_of_arguments != 3:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        answer = add(a, b)
    elif argv[2] == "-":
        answer = sub(a, b)
    elif argv[2] == "*":
        answer = mul(a, b)
    elif argv[2] == "/":
        answer = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {argv[2]} {b} = {answer}")
