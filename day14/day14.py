# Advent of Code day14
import re

def num2bin(n):
    # Converts an integer to a 36 bit bitarray

    binarray = []
    while n > 0:
        binarray.append(n%2)
        n = n // 2

    while len(binarray) < 36:
        binarray.append(0)

    binarray = binarray[::-1]
    return binarray

def bin2num(barray):
    # Converts a bitarray to an integer
    barray = barray[::-1]
    n = sum([pow(2, i) for (i, b) in enumerate(barray) if b == 1])

    return n

def applyMask1(value, mask, location, memory):
    # Apply bitmask to value and then assign masked value to memory location

    bitarray = num2bin(value)

    for i in range(len(mask)):
        if mask[i] == '1':
            bitarray[i] = 1
        elif mask[i] == '0':
            bitarray[i] = 0

    memory[location] = bin2num(bitarray)

def applyMask2(location, mask):
    # Apply mask to location
    bitarray = num2bin(location)

    for i in range(len(mask)):
        if mask[i] == '1':
            bitarray[i] = 1
        elif mask[i] == 'X':
            bitarray[i] = 'X'

    return bitarray 

def updateMemory(location, memory, value):

    if 'X' not in location:
        loc = bin2num(location)
        memory[loc] = value
        return

    idx = location.index('X')
    location[idx] = 1
    updateMemory(location, memory, value)
    location[idx] = 0
    updateMemory(location, memory, value)
    location[idx] = 'X'

    return

def parseProgramme(programme):
    mask = 'X' * 36
    memory = {}

    pat = re.compile('(\d)+')

    for line in programme:
        if line[0] == 'mask':
            mask = line[1]
        else:
            location = int(pat.search(line[0]).group(0))
            value = int(line[1])
            
            # Part 1
            # applyMask1(value, mask, location, memory)

            # Part2
            location = applyMask2(location, mask)
            updateMemory(location, memory, value)


    total = 0
    for k in memory:
        total += memory[k]

    return total
            


if __name__ == "__main__":

    filename = "day14.in"
    programme = []
    with open(filename) as f:
        for line in f:
            instruction = line.rstrip().split(' = ')
            programme.append(instruction)

    total = parseProgramme(programme)
    print(total)
