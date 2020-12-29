def findAdjacent(layout, i, j):
    height = len(layout)
    width = len(layout[0])

    assert i > 0 and i < height-1
    assert j > 0 and j < width-1
    
    neighbours = [line[j-1:j+2] for line in layout[i-1:i+2]]
    neighbours = [el for line in neighbours for el in line]
    neighbours = neighbours[:4] + neighbours[5:]

    return neighbours

def findInview(layout, i, j, height, width, cell):
    # Find all cells that are visible from i,j, that is, all cells (x,y)
    # such that x == i or y ==j, or x-i == y-j

    nOccupied = 0
    # East
    for k in range(i+1, width):
        cell = layout[i][k]
        if cell == 'L':
            break
        elif cell == '#':
            nOccupied += 1
            break
        else:
            layout[i][k] == 'X'

    # South-East
    d = min(height-i, width-j)
    for k in range(1, d):
        cell = layout[i+k][j+k]
        if cell == 'L':
            break
        elif cell == '#':
            nOccupied += 1
            break

    # South
    for k in range(j+1, height):
        cell = layout[k][j]
        if cell == 'L':
            break
        elif cell == '#':
            nOccupied += 1
            break

    # South-West
    d = min(height-i, j+1)
    for k in range(1,d):
        cell = layout[i+k][j-k]
        if layout[i+k][j-k] == 'L':
            break
        elif layout[i+k][j-k] == '#':
            nOccupied += 1
            break

    # West
    for k in range(j-1,-1):
        cell = layout[i][k]
        if cell == 'L':
            break
        elif cell == '#':
            nOccupied += 1
            break

    # North-West
    d = min(i+1, j+1)
    for k in range(1, d):
        cell = layout[i-k][j-k]
        if cell == 'L':
            break
        elif cell == '#':
            nOccupied += 1
            break

    # North
    for k in range(i-1, -1):
        cell = layout[k][j]
        if cell == 'L':
            break
        elif cell == '#':
            nOccupied += 1
            break

    # North-East
    d = min(i+1, width-j)
    for k in range(1, d):
        cell = layout[i-k][j+k]
        if cell == 'L':
            break
        elif cell == '#':
            nOccupied += 1
            break
    
    return nOccupied

def nextRound(layout):

    height = len(layout)
    width = len(layout[0]) 
    change = False

    nextLayout = [['.' for _ in range(width)] for _ in range(height)]
    for i in range(1, height-1):
        for j in range(1, width - 1):
            # Find neighbours for part 1
            # neighbours = findAdjacent(layout, i, j)

            # Find neighbours for part 2
            cell = layout[i][j]
            numOccupied = findInview(layout, i, j, height, width, cell)
            neighbours = ['#' for _ in range(numOccupied)]

            if cell == '.':
                nextLayout[i][j] = '.'
            elif cell == 'L':
                # If the cell is an empty seat, it becomes occupied if 
                # there are no adjacent occupied seats. Otherwise it remains
                # empty
                if neighbours.count('#') == 0:
                    nextLayout[i][j] = '#'
                    change = True
                else:
                    nextLayout[i][j] = 'L'
            elif cell == '#':
                # If there are 4 (5 for part 2) or more adjacent occupied seats, 
                # seat becomes empty
                if neighbours.count('#') >= 5:
                    nextLayout[i][j] = 'L'
                    change = True
                else:
                    nextLayout[i][j] = '#'


    return (nextLayout, change)

def parseInput(infile):
    # Read in the input file, pad on all sides with empty floor space

    layout = []
    with open(infile) as f:
        for line in f:
            line = line.rstrip()
            line = '.' + line + '.'
            layout.append(list(line))

    width = len(layout[0])
    padding = '.'*width
    layout.insert(0, padding)
    layout.append(padding)

    return layout

if __name__ == "__main__":

    infile = "day11.test"
    layout = parseInput(infile)

#    change = True
#    while change:
#        layout, change = nextRound(layout)
#        print('----- next -----')
#        for line in layout:
#            print(''.join(line))
#
#
#    counter = [1 for line in layout for el in line if el == '#']
#    print(sum(counter))
