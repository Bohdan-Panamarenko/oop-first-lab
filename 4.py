import sys

capacity = int(sys.argv[1])
weights = sys.argv[2].split(' ')

def bagProblem(capacity, weights):
    possibleCapacities = [1] + [0] * capacity # make list of all possible capacities

    for i in range(len(weights)): # iterate on all weights
        possibleCapacities_new = possibleCapacities.copy() # make new list to be changed

        for j in range(len(possibleCapacities)): # iterate on possible capacities
            # if we can add this weight to any existed before capacity then mark new capacity
            if possibleCapacities[j - int(weights[i])] == 1: 
                possibleCapacities_new[j] = 1

        possibleCapacities = possibleCapacities_new

    end = len(possibleCapacities) - 1
    while possibleCapacities[end] != 1: # get maximum capacity
        end -= 1
    
    return end

print(bagProblem(capacity, weights))

