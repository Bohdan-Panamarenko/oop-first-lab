import sys

sign = ["+", "-"]

exp = sys.argv[1] # get arguments

prevCharIsNum = True
expIsValid = True
answ = None
lenOfExp = len(exp)

if lenOfExp == 0 or lenOfExp == 1 and not exp[0].isnumeric() or not exp[lenOfExp - 1].isnumeric():
    expIsValid = False
else:
    for element in exp:
        elemIsNum = element.isnumeric()
        elemIsSign = element in sign
        if not elemIsNum and not elemIsSign or not prevCharIsNum and elemIsSign:
            expIsValid = False
            break
        prevCharIsNum = elemIsNum

if expIsValid:
    answ = eval(exp)

print(f"({expIsValid}, {answ})")




