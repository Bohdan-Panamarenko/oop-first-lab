def bestSetRec(args, capacity, currWeight, weight):
    numOfBars = len(weight)

    for index, element in enumerate(weight):
        weightWithElem = currWeight + element

        if weightWithElem <= capacity:
            
            if weightWithElem > args["bestCapacity"]:
                args["bestCapacity"] = element + currWeight

            if index + 1 < numOfBars:
                bestSetRec(args, capacity, weightWithElem, weight[(index + 1):])
        else:
            return

def bestSet(capacity, weights):
    weights.sort()
    numOfBars = len(weights)
    args = {
        "bestCapacity" : 0
    }

    for index, element in enumerate(weights):

        if element <= capacity:

            if element > args["bestCapacity"]:
                args["bestCapacity"] = element

            if index + 1 < numOfBars:
                bestSetRec(args, capacity, element, weights[(index + 1):])
        else:
            break

    return args["bestCapacity"]

print(bestSet(19, [5, 7, 1, 20, 4]))
