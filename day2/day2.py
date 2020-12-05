def oldCheck(low, high, ch, password):
    # Solution to part 1 
    
    count = password.count(ch)
    if count >= low and count <= high:
        return True
    else:
        return False

def newCheck(low, high, ch, password):
    # Solution to part 2

    if password[low-1] == ch and password[high-1] == ch:
        return False
    elif password[low-1] == ch:
        return True
    elif password[high-1] == ch:
        return True
    else:
        return False

if __name__ == "__main__":
    numValid = 0
    with open('day2.in') as f:
        for line in f:
            # Read passwords and constraints
            # line: 'lo-hi ch: pwd'
            data = line.split()
            constraintStr = data[0]
            low, high = list(map(int, constraintStr.split('-')))
            ch = data[1][0]
            password = data[2]
            
            if newCheck(low, high, ch, password):
                numValid += 1

    print(numValid)

