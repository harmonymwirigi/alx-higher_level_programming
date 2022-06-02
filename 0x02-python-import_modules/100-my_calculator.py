#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    if len(sys.argv) - 1 == 3:
        if sys.argv[2] == '+':
            result = add(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == '-':
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == '*':
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == '/':
            result = div(int(sys.argv[1]), int(sys.argv[3]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    print("{:s} {:s} {:s} = {:d}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
