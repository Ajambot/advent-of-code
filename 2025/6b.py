with open('6.txt') as f:
    problems = []
    for line in f:
        problems.append(line[:-1])

    res = 0
    problemQ = []
    skip = False
    op = ""
    for col in range(len(problems[0])-1, -1, -1):
        if skip:
            skip = False
            continue
        num = []
        for row in range(len(problems)):
            if problems[row][col] == " ":
                continue
            if problems[row][col] in ["+", "*"]:
                skip = True
                op = problems[row][col]
            else:
                num.append(problems[row][col])
        problemQ.append(int("".join(num)))
        if skip:
            total = 1 if op == "*" else 0
            for operand in problemQ:
                if op == "*":
                    total *= operand
                else:
                    total += operand
            res += total
            problemQ = []
    print(res)
