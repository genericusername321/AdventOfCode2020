# Advent of Code 2020 day 15

def sol(preamble, n):
    # Computes the nth character of the sequence

    if n < len(preamble):
        return preamble[n]

    # 
    memory = {}
    for i, v in enumerate(preamble[:-1]):
        memory[v] = i

    # 
    lastval = preamble[-1]
    for i in range(len(preamble), n+1):
        if lastval in memory:
            temp = memory[lastval]
            memory[lastval] = i-1
            lastval = i-1 - temp
        else:
            memory[lastval] = i-1
            lastval = 0

    return lastval

if __name__ == "__main__":

    infile = "day15.in"
    with open(infile) as f:
        seq = list(map(int, f.read().rstrip().split(',')))
    
    # part 1
    val1 = sol(seq, 2019)
    print("part 1: ", val1)
    
    # part 2
    val2 = sol(seq, 29999999)
    print("part 2: ", val2)
