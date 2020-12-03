

def getFormattedInput(filename):
    return [[isTree == "#" for isTree in x] for x in open(filename, "r").read().split("\n")]

def solve3a(inputMatrix, slope):
    i, j = [0, 0]
    numTrees = 0
    while i <= len(inputMatrix) - 1:
        if inputMatrix[i][j]:
            numTrees += 1
        j = (j + slope[0]) % len(inputMatrix[0])
        i += slope[1]
        
    return numTrees

def solve3b(inputMatrix, slopeList):
    product = 1
    for x in slopeList:
        product = product * solve3a(inputMatrix, x)
    
    return product



print(solve3a(getFormattedInput("input.txt"), [3, 1]))

slopeList = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(solve3b(getFormattedInput("input.txt"), slopeList))
