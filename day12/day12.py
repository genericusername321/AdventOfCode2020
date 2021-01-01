# Advent of code day12
import numpy as np

def part1(instructions):

    # Encode directions as unit vectors
    directionMap = {'E' : 0, 'S' : 1, 'W' : 2, 'N' : 3}
    vectors = [np.array([1,0]), np.array([0,-1]), np.array([-1,0]), np.array([0,1])]

    curpos = np.array([0,0])
    heading = 0

    for action, value in instructions:

        if action == 'L':
            heading = (heading + 4 - value // 90) % 4
        elif action == 'R':
            heading = (heading + value // 90) % 4
        else:
            if action == 'F':
                d = heading
            else:
                d = directionMap[action]

            curpos = curpos + vectors[d] * value

    return curpos

def part2(instructions):
    # Solve part 2

    curpos = np.array([0,0])
    waypoint = np.array([10, 1])
    R = np.array([[0,1],[-1,0]])
    L = np.array([[0,-1],[1,0]])
    
    directionmap = {'E' : np.array([1,0]), 
            'S' : np.array([0,-1]),
            'W' : np.array([-1,0]),
            'N' : np.array([0,1])}


    for action, value in instructions:
        if action == 'L':
            # Rotate waypoint left 
            n = value // 90
            waypoint = np.matmul(np.linalg.matrix_power(L, n), waypoint)
        elif action == 'R':
            # Rotate waypoint right
            n = value // 90
            waypoint = np.matmul(np.linalg.matrix_power(R, n), waypoint)
        elif action == 'F':
            curpos = curpos + value * waypoint
        else:
            waypoint = waypoint + value * directionmap[action]

    return curpos
    
def parseInput(filename):

    instructions = []
    with open(filename) as f:
        for line in f:
            line.rstrip()
            action = line[:1]
            value = int(line[1:])
            instructions.append((action, value))

    return instructions

if __name__ == "__main__":

    filename = "day12.in"
    instructions = parseInput(filename)

    pos1 = part1(instructions)
    print(abs(pos1[0]) + abs(pos1[1]))

    pos2 = part2(instructions)
    print(abs(pos2[0]) + abs(pos2[1]))
