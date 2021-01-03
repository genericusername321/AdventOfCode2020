# Advent of code 2020, day 13
from functools import reduce


def egcd(a, b):
    # Extended euclidean algorithm, returns (g, x, y) where
    #   g = gcd(a,b)
    # and x, y are such that
    #   g = x*a + y*b

    # Implementation copied from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Iterative_algorithm_3

    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def mul_inv(a, b):
    # Find multiplicative inverse of a, modulo b, i.e. find x such that
    #   a*x = 1 mod b

    _, r, _ = egcd(a, b)

    return r

def chinese_remainder(n, a):
    # Solve system of modular equations 
    # Implemetation from wikibooks

    total = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p

    return total % prod


def part1(time, departures):
    # Note that the wait time from time T for a given service S
    # can be computed by W = S - T % S. T % S indicates the number of 
    # minutes that have passed since the last departure of service S

    # Filter x from departure times
    departures = list(filter(lambda x : x != 'x', departures))
    departures = list(map(int, departures))

    waittimes = list(map(lambda x : x - (time % x), departures))

    mintime = min(waittimes)
    service = departures[waittimes.index(mintime)]

    return mintime * service 

def part2(departures):
    # Find minimal t such that:
    #   t mod a[i] = i
    # whenever a[i] != x.
    # 
    # Compute the solution using the Chinese remainder theorem

    # List departure times and index in list:
    departures = [(t[0], int(t[1])) for t in enumerate(departures) if t[1] != 'x']

    a = [(s-t) % s for t, s in departures]
    n = [t for s, t in departures]

    return chinese_remainder(n, a)


if __name__ == "__main__":

    filename = "day13.in"
    with open(filename) as f:
        # Read earliest departure time
        time = int(f.readline())
        services = f.readline().rstrip().split(',')

    sol1 = part1(time, services)
    print("-- part 1 --")
    print(sol1)

    print("-- part 2 --")
    print(part2(services))


