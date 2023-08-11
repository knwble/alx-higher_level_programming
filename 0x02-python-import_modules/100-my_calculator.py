#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    len_args = len(argv)
    if len_args != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    functions_basics = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in functions_basics:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, functions_basics[op]
                                             (a, b)))
        exit(0)
