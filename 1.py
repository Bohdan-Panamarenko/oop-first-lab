import sys
from operator import add, sub, mul, truediv

exp = sys.argv # get arguments
exp.pop(0) # remove filename

# math operators
addSubOperators = {
    "+" : add,
    "-" : sub
}

mulDivOperators = {
    "*" : mul,
    "/" : truediv
}

# perform multiplication and division first
index = 0
while index < len(exp):
    mulDivFunc = mulDivOperators.get(exp[index])
    if mulDivFunc:
        exp[index] = mulDivFunc(float(exp[index - 1]), float(exp[index + 1]));
        exp.pop(index + 1)
        exp.pop(index - 1)
    else:
        index += 1

# then perform summing and substracting
index = 0
while index < len(exp):
    addSubFunc = addSubOperators.get(exp[index])
    if addSubFunc:
        exp[index] = addSubFunc(float(exp[index - 1]), float(exp[index + 1]));
        exp.pop(index + 1)
        exp.pop(index - 1)
    else:
        index += 1


print(exp[0])