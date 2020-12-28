def fix(programme):
    """
    Note that the nops and jumps that we need to fix must be one
    that is visited in the erroneous execution.
        1. Find all nops and jumps along the executed lines
        2. Do brute force search on all nops and jumps to see if programme
           terminates correctly.
    """
    nops, jumps = findNopsAndJumps(programme)
    n = len(programme)

    for nop in nops:
        programme[nop][0] = 'jmp'
        total, c = run(programme)
        if c == n:
            return total
        programme[nop][0] = 'nop'

    for jmp in jumps:
        programme[jmp][0] = 'nop'
        total, c = run(programme)
        if c == n:
            return total
        programme[jmp][0] = 'jmp'

def findNopsAndJumps(programme):
    """
    Find all visited nop and jump commands
    """

    nops = []
    jumps = []
    
    visited = []    # visited lines
    pointer = 0     # current line
    n = len(programme)


    while pointer < n and pointer >= 0 and pointer not in visited:
        ins, arg = programme[pointer]
        visited.append(pointer)
        if ins == 'nop':
            # No operation, go to next line
            nops.append(pointer)
            pointer += 1
        elif ins == 'acc':
            # Increase accumulator by argument, then go to next line
            pointer += 1
        elif ins == 'jmp':
            # Jump to new instruction at distance arg from current line
            jumps.append(pointer)
            pointer += arg

    return (nops, jumps)

def run(programme):
    """
    Find the accumulator value before the programme enters the infinite loop.
    Keep a list of all visited lines, print the value of the accumulator when the
    next line is in the list of visited lines.
    """

    accumulator = 0       # accumulator value
    pointer = 0           # current line
    size = len(programme)
    visited = []        # visited lines
    while pointer < size and pointer >= 0 and pointer not in visited:
        ins, arg = programme[pointer]

        visited.append(pointer)
        if ins == 'nop':
            # No operation, go to next line
            pointer += 1
        elif ins == 'acc':
            # Increase accumulator by argument, then go to next line
            pointer += 1
            accumulator += arg
        elif ins == 'jmp':
            # Jump to new instruction at distance arg from current line
            pointer += arg

    return (accumulator, pointer)


def parseInput(infile):

    # Parse the instructions into a programme
    
    programme = []
    with open(infile) as f:
        for line in f:
            instruction, argument = line.split(' ')
            programme.append([instruction, int(argument)])
            
    return programme

if __name__ == "__main__":

    programme = parseInput("day8.in")

    # part 1
    print(run(programme))
    print(fix(programme))
