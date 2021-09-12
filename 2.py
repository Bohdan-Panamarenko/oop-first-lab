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

binaryFunc = binaryOperators.get(exp[0])
unaryFunc = unaryOperators.get(exp[0])
answ = None

if binaryFunc:
    if exp[1] and exp[2]:
        answ = binaryFunc(float(exp[1]), float(exp[2]))
    else:
        print("Not enough arguments for function {exp[0]}")
elif unaryFunc:
    if exp[1]:
        answ = unaryFunc(float(exp[1]))
    else:
        print("Not enough arguments for function {exp[0]}")
else:
    print("Unknown function {exp[0]}")

print(answ)
