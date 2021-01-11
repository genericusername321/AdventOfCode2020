# Read the input 
import numpy as np

def parseInput(infile):

    with open(infile) as f:
        data = [line.strip() for line in f]

    return data

def part1(data, N):

    dataX = len(data[0])
    dataY = len(data)

    # dimensions
    z = 1 + 2 * N 
    x = dataX + 2 * N 
    y = dataY + 2 * N 

    # cube is a 3d array of size z x y x x
    cubes = np.zeros((z,y,x), dtype=np.int8)
    for ii in range(dataY):
        for jj in range(dataX):
            if data[ii][jj] == '#':
                cubes[N][ii+N][jj+N] = 1
            else:
                cubes[N][ii+N][jj+N] = 0
    
    # Do iterations
    for step in range(1, N):
        # Consider only the cubes that can be reached in N steps
        newcube = np.zeros((z,y,x), dtype=np.int8)
        for iz in range(1, z-1):
            for ix in range(1, x-1):
                for iy in range(1, y-1):
                    neighbours = cubes[iz-1:iz+2, iy-1:iy+2, ix-1:ix+2]
                    
                    # Count number of activated neighbours
                    activatedNeighbours = np.sum(neighbours) - neighbours[1,1,1]
                    
                    if cubes[iz, iy, ix] == 1:
                        if activatedNeighbours in {2,3}:
                            newcube[iz, iy, ix] = 1 
                        else:
                            newcube[iz, iy, ix] = 0

                    elif activatedNeighbours == 3:
                        newcube[iz, iy, ix] = 1
        
        cubes = newcube[:]

    return np.sum(newcube)

def part2(data, N):

    dataX = len(data[0])
    dataY = len(data)

    # dimensions
    w = 1 + 2 * N
    z = 1 + 2 * N 
    x = dataX + 2 * N 
    y = dataY + 2 * N 

    # cube is a 4d array of size w x z x y x x
    cubes = np.zeros((w,z,y,x), dtype=np.int8)
    for ii in range(dataY):
        for jj in range(dataX):
            if data[ii][jj] == '#':
                cubes[N][N][ii+N][jj+N] = 1
            else:
                cubes[N][N][ii+N][jj+N] = 0
    
    # Do iterations
    for step in range(1, N):
        # Consider only the cubes that can be reached in N steps
        newcube = np.zeros((w,z,y,x), dtype=np.int8)
        for iw in range(1, w-1):
            for iz in range(1, z-1):
                for ix in range(1, x-1):
                    for iy in range(1, y-1):
                        neighbours = cubes[iw-1:iw+2, iz-1:iz+2, iy-1:iy+2, ix-1:ix+2]
                        
                        # Count number of activated neighbours
                        activatedNeighbours = np.sum(neighbours) - neighbours[1,1,1,1]
                        
                        if cubes[iw, iz, iy, ix] == 1:
                            if activatedNeighbours in {2,3}:
                                newcube[iw, iz, iy, ix] = 1 
                            else:
                                newcube[iw, iz, iy, ix] = 0

                        elif activatedNeighbours == 3:
                            newcube[iw, iz, iy, ix] = 1
        
        cubes = newcube[:]

    return np.sum(newcube)

if __name__ == "__main__":

    with open("day17.in") as f:
        data = [line.strip() for line in f]

    nactive = part1(data, 7)
    print(nactive)

    nactive = part2(data, 7)
    print(nactive)
