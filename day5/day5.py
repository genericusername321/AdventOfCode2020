
def parseBoardingPass(boardingPass):
    # Solution to part 1
    rowStr = boardingPass[:7]
    seatStr = boardingPass[7:]

    rowStr = rowStr.replace('F', '0')
    rowStr = rowStr.replace('B', '1')
    row = int(rowStr, 2)

    seatStr = seatStr.replace('L', '0')
    seatStr = seatStr.replace('R', '1')
    seat = int(seatStr, 2)

    seatId = 8 * row + seat
    return seatId

if __name__ == "__main__":
    with open('day5.in') as f:
        passes = [element for line in f for element in line.split()]

    seatIds = list(map(parseBoardingPass, passes))
    maxSeatId = max(seatIds)
    print(maxSeatId)
    
    seatIds.sort()
    for i in range(len(seatIds)-1):
        if seatIds[i+1] - seatIds[i] == 2:
            print(seatIds[i]+1)
