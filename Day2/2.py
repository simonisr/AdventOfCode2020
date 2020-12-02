


def getNumberList(filename):
    return [x.split(" ") for x in open(filename, "r").read().split("\n")]
    
def solve2a(inputList):
    numValid = 0
    for x in inputList:
        minVal, maxVal = [int(y) for y in x[0].split("-")]
        charCount = x[2].count(x[1][0])
        if charCount >= minVal and charCount <= maxVal:
            numValid += 1
    return numValid
    
def solve2b(inputList):
    numValid = 0

    for x in inputList:
        firstPos, secondPos = [int(y) for y in x[0].split("-")]
        targetChar = x[1][0]
        if (x[2][firstPos-1] == targetChar) != (x[2][secondPos-1] == targetChar):
            numValid += 1
    return numValid

print(solve2a(getNumberList("input.txt")))

print(solve2b(getNumberList("input.txt")))