# Advent of code 2020, day 7
import re

def parseInput(infile):
    rules = {}
    patbag = re.compile('[a-z\s]+(?=bag)')
    patnum = re.compile('[0-9]+')
    with open(infile) as f:
        for line in f:
            # Remove trailing newline
            line = line.rstrip()
            line = line.replace('bags', 'bag')
            line = line.split('contain')

            # Find the bag description the rule applies to
            bagstr = line[0]
            bag = patbag.match(bagstr).group()
            bag = bag.lstrip()
            bag = bag.rstrip()

            # Find the contents of the bag
            contentlist = []
            contentstr = line[1].split(',')
            for content in contentstr:
                # Find the number of bags
                number = patnum.findall(content)
                bagtype = patbag.findall(content)
                bagtype = bagtype[0]
                bagtype = bagtype.lstrip()
                bagtype = bagtype.rstrip()
                if bagtype == 'no other':
                    continue

                number = int(number[0])
                t = (bagtype, number)
                contentlist.append(t)

            rules[bag] = contentlist

    return rules

def countContainingBags(rules, requestedbag):

    # Create new dictionary with reversed membership condition: key denotes 
    # bag type, and values denote the bagtypes the key is contained in.
    revRules = {}
    for outerbag in rules:
        for innerbagTuple in rules[outerbag]:
            bagtype = innerbagTuple[0]
            if not bagtype in revRules:
                revRules[bagtype] = [outerbag]
            else:
                revRules[bagtype].append(outerbag)
    
    # Use DFS to find all legal outer bags of 'shiny gold'
    stack = [requestedbag]
    legalbags = []
    while stack:
        curbag = stack.pop()
        legalbags.append(curbag)
        outerbags = revRules.get(curbag, [])
        for bag in outerbags:
            stack.append(bag)
    
    legalbags.remove(requestedbag)
    legalbags = set(legalbags)

    return len(legalbags)

def countContainedBags(rules, bagtype):

    # Use DFS to find all contained bags
    stack = [(bagtype, 1)]
    contained = {bagtype : 1}
    while stack:
        curbag, curNumber = stack.pop()
        innerbagsTuple = rules[curbag]
        for t in innerbagsTuple:
            bag, number = t
            stack.append((bag, number*curNumber))
            
            if bag in contained:
                contained[bag] += number * curNumber
            else:
                contained[bag] = number * curNumber

    total = 0
    for bagtype in contained:
        total += contained[bagtype]

    return total-1
            



if __name__ == "__main__":

    # Read rules into dictionary, they key denotes the bag type, the value
    # is a list of tuples denoting the number and types the key contains.
    rules = parseInput("day7.in")

    print("part1: ", countContainingBags(rules, 'shiny gold'))

    print("part2: ", countContainedBags(rules, 'shiny gold'))
