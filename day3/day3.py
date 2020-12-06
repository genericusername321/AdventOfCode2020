def countTrees(treemap, stepRow, stepCol):
    # Solution to part 1 and part 2
    nRows = len(treemap)
    nCols = len(treemap[0])
    nTrees = 0

    col = 0
    for rowIndex in range(stepRow,nRows,stepRow):
        row = treemap[rowIndex]
        col = (col + stepCol) % nCols
        if row[col] == '#':
            nTrees += 1

    return nTrees

if __name__ == "__main__":
    with open('day3.in') as f:
        treemap = [line.rstrip() for line in f]

    stepsRow = [1,1,1,1,2]
    stepsCol = [1,3,5,7,1]

    tot = 1
    for k in range(len(stepsRow)):
        tot = tot * countTrees(treemap, stepsRow[k], stepsCol[k])

    print(tot)
