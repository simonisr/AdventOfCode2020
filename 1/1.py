



def getNumberList(filename):
    return [int(x) for x in open(filename, "r").read().split()]

def solve_1a(list, targetSum):
    diffList = [0]*targetSum
    
    for x in list:
        diff = targetSum - x

        if diffList[x] == 1:
            print(diff*x)
            return

        diffList[diff] = 1




solve_1a(getNumberList("input.txt"), 2020)