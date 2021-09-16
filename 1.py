import sys
from operator import add, sub, mul, truediv

exp = sys.argv # get arguments
exp.pop(0) # remove filename

strExp = ""
for element in exp:
    strExp += element

try:
    print(eval(strExp))
except ZeroDivisionError:
    print('Dividision by zero')
except (SyntaxError, NameError, TypeError, ValueError):
    print('Invalid expression')
