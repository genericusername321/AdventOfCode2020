def findAdjacent(layout, i, j):
    # Find adjacent cells
    height = len(layout)
    width = len(layout[0])

    assert i > 0 and i < height-1
    assert j > 0 and j < width-1
    
    neighbours = [line[j-1:j+2] for line in layout[i-1:i+2]]
    neighbours = [el for line in neighbours for el in line]

    # Remove middle cell itself
    neighbours = neighbours[:4] + neighbours[5:]

    return neighbours

def findView(layout, i, j, height, width):
    # Find the seats that are visible from location [i][j]

    neighbours = []
    locations = []
    seats = {'L', '#'}


    # Look north
    for k in range(i-1, 0, -1):
        cell = layout[k][j]
        if cell in seats:
            neighbours.append(cell)
            locations.append((k,j))
            break
    
    # Look east
    for k in range(j+1, width):
        cell = layout[i][k]
        if cell in seats:
            neighbours.append(cell)
            locations.append((i,k))
            break
    
    # Look south
    for k in range(i+1, height):
        cell = layout[k][j]
        if cell in seats:
            neighbours.append(cell)
            locations.append((k,j))
            break

    # Look west
    for k in range(j-1, 0, -1):
        cell = layout[i][k]
        if cell in seats:
            neighbours.append(cell)
            locations.append((i,k))
            break

    # Look north-east
    d = min(i, width - (j+1))
    for k in range(1,d):
        cell = layout[i-k][j+k]
        if cell in seats:
            neighbours.append(cell)
            locations.append((i-k, j+k))
            break

    # Look south-east
    d = min(height - (i+1), width - (j+1))
    for k in range(1,d):
        cell = layout[i+k][j+k]
        if cell in seats:
            neighbours.append(cell)
            locations.append((i+k, j+k))
            break

    # Look south-west
    d = min(height - (i+1), j)
    for k in range(1,d):
        cell = layout[i+k][j-k]
        if cell in seats:
            neighbours.append(cell)
            locations.append((i+k, j-k))
            break

    # north-west
    d = min(i, j)
    for k in range(1,d):
        cell = layout[i-k][j-k]
        if cell in seats:
            neighbours.append(cell)
            locations.append((i-k, j-k))
            break

    return neighbours


def iterate(layout):

    height = len(layout)
    width = len(layout[0]) 
    change = False

    # Create next iteration
    nextLayout = [['.' for _ in range(width)] for _ in range(height)]
    for i in range(1, height-1):
        for j in range(1, width - 1):
            # Find neighbours for part 1
            # neighbours = findAdjacent(layout, i, j)

            # Find neighbours for part 2
            cell = layout[i][j]
            neighbours = findView(layout, i, j, height, width)

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

    infile = "day11.in"
    layout = parseInput(infile)

    print('----- original -----')
    for line in layout:
        print(''.join(line))


    change = True
    while change:
        layout, change = iterate(layout)


    counter = [1 for line in layout for el in line if el == '#']
    print(sum(counter))
