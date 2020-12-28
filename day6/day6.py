def countAnswers(groupAns):
    # Solution for part1 and part2
    total = 0
    for ans in groupAns:
        ans = ans.rstrip().split('\n')
        answers = [set(a) for a in ans]

        # Replace union with intersection for part 2
        union = answers[0].union(*answers)
        total += len(union)

    return total



if __name__ == "__main__":
    with open('day6.in') as f:
        data = f.read()

    # Find group answers splitting by newline
    groupAns = data.split('\n\n')
    print(countAnswers(groupAns))

