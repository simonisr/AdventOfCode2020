
def getInputData(fileName):
    return open(fileName).read().split("\n\n")
    
def getPersonSum(inputString, groupAnswers):
    answers = groupAnswers.copy()
    for c in inputString:
        if c not in answers:
            answers[c] = 1
        else:
            answers[c] += 1
    return answers

def getGroupSum(inputString):
    groupAnswers = {}
    for p in inputString.split("\n"):
        groupAnswers = getPersonSum(p, groupAnswers)
    return len(groupAnswers)

def getNumOfGroupOverlap(inputString):
    groupAnswers = {}
    groupInput = inputString.split("\n")
    for p in groupInput:
        groupAnswers = getPersonSum(p, groupAnswers)
    return len([x for x in groupAnswers if groupAnswers[x] == len(groupInput)])

def solve6a(inputData):
    totalSum = 0
    for g in inputData:
        totalSum += getGroupSum(g)
    return totalSum

def solve6b(inputData):
    totalSum = 0
    for g in inputData:
        totalSum += getNumOfGroupOverlap(g)
    return totalSum

print(solve6a(getInputData("input.txt")))

print(solve6b(getInputData('input.txt')))