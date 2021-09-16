import operator
import sys
from operator import add, sub, mul, truediv
from math import sin, cos, tan, atan

exp = sys.argv # get arguments
exp.pop(0) # remove filename

# math operators
binaryOperators = {
    "add" : add,
    "sub" : sub,
    "mul" : mul,
    "truediv" : truediv
}

unaryOperators = {
    "sin" : sin,
    "cos" : cos,
    "tan" : tan,
    "atan" : atan
}


try:
    binaryFunc = binaryOperators.get(exp[0])
    unaryFunc = unaryOperators.get(exp[0])
    argOne = exp[1]
    answ = None


    if binaryFunc:
        if exp[2]:
            answ = binaryFunc(float(exp[1]), float(exp[2]))
    elif unaryFunc:
        answ = unaryFunc(float(exp[1]))
    else:
        print(f"Unknown function: {exp[0]}")

    if answ:
        print(answ)
except ZeroDivisionError:
    print('division by zero')
except IndexError:
    print('not enough arguments')
except ValueError:
    print('unvalid value')

