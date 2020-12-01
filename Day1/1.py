# Read input from text file called input.txt
def getNumberList(filename):
    return [int(x) for x in open(filename, "r").read().split()]

# Solution to first problem
def solve1a(inputList, targetSum):
    diffList = [0]*(targetSum + 1)
    
    for x in inputList:

        if x >= targetSum:
            continue

        diff = targetSum - x

        if diffList[x] == 1:
            return diff*x

        diffList[diff] = 1
    
    return -1

# Returns a list of differences based on a target sum and a list of values < target sum
def getDiffList(inputList, targetSum):
    return [targetSum - x for x in inputList]

# Solution to problem 2
def solve1b(inputList, targetSum):

    diffList = getDiffList(inputList, targetSum)

    for newSum in diffList:
        partialAns = solve1a(inputList, newSum)

        if partialAns > 0:
            return partialAns*(targetSum-newSum)


# Answer day 1 problem 1
print(solve1a(getNumberList("input.txt"), 2020))

#Answer day 1 problem 2
print(solve1b(getNumberList("input.txt"), 2020))