with open('6.txt') as f:
    problems = []
    for line in f:
        problems.append(line.strip().split())

    res = 0
    for col in range(len(problems[0])):
        op = problems[-1][col]
        total = 0 if op == "+" else 1
        for row in range(len(problems)-1):
            if op == "+":
                total += int(problems[row][col])
            else:
                total *= int(problems[row][col])
        res += total
    print(res)
