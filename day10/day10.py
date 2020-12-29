
def computeArrangements(arr):
    """
    Compute the number of ways the adapters can be arranged to connect
    the device to the wall socket.

    Using a dynamic programming strategy, let P[i] be the number of ways 
    to connect the wall socket to adapter with rating i. Then P[0] = 1, and 
    for i > 0 and i in arr, P[i] = P[i-1] + P[i-2] + P[i-3]
    """
    
    maxRating = max(arr)
    P = [0]*(maxRating+5)
    P[0] = 1

    for i in arr[1:]:
        P[i] = P[i-1] + P[i-2] + P[i-3]

    return P[arr[-1]]
    

def diff(arr):
    """
    Compute difference array of the given array, i.e.
    delta[i] = arr[i+1] - arr[i]
    """

    size = len(arr)
    delta = [0] * (size-1)
    for i in range(size-1):
        delta[i] = arr[i+1] - arr[i]

    return delta

if __name__ == "__main__":

    infile = "day10.in"
    with open(infile) as f:
        adapters = [int(line.rstrip()) for line in f]
    
    adapters.append(max(adapters)+3)    # add device rating
    adapters.append(0)                  # add wallsocket rating
    adapters.sort()

    # Part 1 solution
    delta = diff(adapters)
    print("#1:\t", delta.count(1))
    print("#3:\t", delta.count(3))
    print(delta.count(1) * delta.count(3))
    
    numpaths = computeArrangements(adapters)
    print("Number of arrangements:\t", numpaths)
