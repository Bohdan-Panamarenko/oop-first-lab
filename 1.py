import sys
from operator import add, sub, mul, truediv

exp = sys.argv # get arguments
exp.pop(0) # remove filename

strExp = ""
for element in exp:
    strExp += element

print(eval(strExp))