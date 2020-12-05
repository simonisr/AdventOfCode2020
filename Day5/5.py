
def getSeatSpecifications(fileName):
    return open(fileName).read().split()

def getReducedValue(reductionKey, maxValue):
    lowValues = ['F', 'L']
    low = 0
    high = maxValue
    for c in reductionKey[0:len(reductionKey)-1]:
        if(c in lowValues):
            high = high - (high - low) // 2 if high % 2  == 0 else high - 1 - (high - low) // 2
        else:
            low = low + (high - low) // 2 if high % 2 == 0 else  1 + low + (high - low) // 2

    return low if reductionKey[-1] in lowValues else high

def getRowValue(seatSpecification):
    return getReducedValue(seatSpecification[:8], 127)

def getColumnValue(seatSpecification):
    return getReducedValue(seatSpecification[7:], 7)

def getSeatID(seatSpecification):
    return getRowValue(seatSpecification)*8 + getColumnValue(seatSpecification)

def solve5a(seatSpecificationList):
    maxSeatID = 0
    for spec in seatSpecificationList:
        id = getSeatID(spec)
        maxSeatID = id if id > maxSeatID else maxSeatID
    return maxSeatID

def solve5b(seatSpecificationList):
    takenSeatList = [0]*(solve5a(seatSpecificationList) +1)
    
    for i in range(0, len(seatSpecificationList)):
        seatID = getSeatID(seatSpecificationList[i])
        takenSeatList[seatID] = 1
    
    firstTakenSeat = takenSeatList.index(1)
    mySeatID = takenSeatList.index(0, firstTakenSeat)

    return mySeatID


print(solve5a(getSeatSpecifications("input.txt")))

print(solve5b(getSeatSpecifications("input.txt")))
