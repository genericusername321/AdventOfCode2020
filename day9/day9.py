def findError(sequence, memory):
    size = len(sequence)

    for i in range(memory, size):
        preamble = sequence[i-memory:i+1]
        legalnums = [i+j for i in preamble for j in preamble]
        if sequence[i] not in legalnums:
            return sequence[i]

    return None

def findSubsetSum(sequence, target):
    size = len(sequence)

    lpointer = 0
    rpointer = 0
    total = sequence[0]

    while total != target:
        if total < target:
            rpointer += 1
            total += sequence[rpointer]
        else:
            total -= sequence[lpointer]
            lpointer += 1

    return sequence[lpointer:rpointer+1]

    

def readSequence(infile):
    with open(infile) as f:
        sequence = [int(line.rstrip()) for line in f]

    return sequence

if __name__ == "__main__":

    sequence = readSequence("day9.in")

    number = findError(sequence, 25)
    subset = findSubsetSum(sequence, number)
    print(number)
    print(min(subset) + max(subset))

