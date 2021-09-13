import sys

capacity = int(sys.argv[1])
weights = sys.argv[2].split(' ')

def bagProblem(capacity, weights):
    possibleCapacities = [1] + [0] * capacity

    for i in range(len(weights)):
        possibleCapacities_new = possibleCapacities.copy()

        for j in range(len(possibleCapacities)):
            if possibleCapacities[j - int(weights[i])] == 1:
                possibleCapacities_new[j] = 1

        possibleCapacities = possibleCapacities_new

    end = len(possibleCapacities) - 1
    while possibleCapacities[end] != 1:
        end -= 1
    
    return end

print(bagProblem(capacity, weights))

