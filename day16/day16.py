# Advent of Code 2020 day 16
from functools import reduce

def parseInput(filename):

    with open(filename) as f:
        data = f.read().split('\n\n')

    # parse the constraints
    constraints = {}
    for line in data[0].split('\n'):
        field, values = line.split(': ')
        values = values.split(' or ')
        first = tuple(map(int, values[0].split('-')))
        second = tuple(map(int, values[1].split('-')))

        constraints[field] = (first, second)

    # Parse personal ticket
    _, ticket = data[1].split('\n')
    myTicket = list(map(int, ticket.split(',')))

    # Parse other tickets
    _, *tickets = data[2].rstrip().split('\n')
    otherTickets = []
    for line in tickets:
        ticket = tuple(map(int, line.split(',')))
        otherTickets.append(ticket)

    return constraints, myTicket, otherTickets

def validateFields(number, constraints):
    # Check for which fields the number is a valid quantity

    validFields = []
    for k, v in constraints.items():
        constrA, constrB = v
        rangeA = range(constrA[0], constrA[1]+1)
        rangeB = range(constrB[0], constrB[1]+1)

        if number in rangeA or number in rangeB:
            validFields.append(k)

    return set(validFields)

def validateTicket(ticket, constraints):
    # Determines the validity of the ticket given a set of constraints.
    # A ticket is valid if each fields satisfies at least one constraint.
    # Conversely the ticket is invalid if at least one fields satisfies no
    # constraint.

    for number in ticket:
        if not validateFields(number, constraints):
            return False

    return True

def part2(tickets, constraints):
    # Determine which column of the ticket data corresponds to which field 
    # of the constraints
    # 
    # For each number, determine the fields for which it would be valid. The correct
    # field is the field that is valid for all numbers of that column

    # Filter out only the valid tickets
    validTickets = [t for t in tickets if validateTicket(t, constraints) is True]

    # Reshape data 
    nFields = len(constraints)
    ticketdata = []
    for i in range(nFields):
        field = [ticket[i] for ticket in validTickets]
        ticketdata.append(field)
    
    # Determine potential fieldnames for each field. A fieldname potentially fits the 
    # column if all numbers fit the constraints corresponding to that fieldname
    potentialFieldnames = {}
    for index, field in enumerate(ticketdata):
        validFields = [validateFields(num, constraints) for num in field]
        fieldname = reduce(lambda x, y: x.intersection(y), validFields)
        potentialFieldnames[index] = fieldname
        
    # Now determine all the fieldnames
    allFieldnames = set(constraints.keys())
    fieldnames = {}
    while allFieldnames:
        for k, v in potentialFieldnames.items():
            # Compute intersection of remaining field names and potential field names
            field = v.intersection(allFieldnames)
            if len(field) == 1:
                field = next(iter(field))
                fieldnames[k] = field
                allFieldnames.remove(field)
    
    return fieldnames


def part1(tickets, constraints):

    total = 0

    for ticket in tickets:
        for number in ticket:
            isValid = False
            for _, v in constraints.items():
                constrA, constrB = v
                rangeA = range(constrA[0], constrA[1]+1)
                rangeB = range(constrB[0], constrB[1]+1)
                
                if number in rangeA or number in rangeB:
                    isValid = True
                    break
            
            if not isValid:
                total += number

    return total 

if __name__ == "__main__":
    
    # Parse puzzle input
    filename = "day16.in"
    constraints, myTicket, otherTickets = parseInput(filename)

    # Part 1 solution
    errorRate = part1(otherTickets, constraints)
    print(errorRate)

    # Part 2 solution
    fields = part2(otherTickets, constraints)

    total = 1
    for k, v in fields.items():
        if 'departure' in v:
            total *= myTicket[k]

    print(total)

