with open('3.txt') as f:
    res = 0
    for line in f:
        line = line.strip()
        l, r = 0, 1
        highest = -1
        for i, c in enumerate(line):
            if i == 0:
                continue
            if c > line[l] and i != len(line)-1:
                l, r = i, i+1
            else:
                r = i
            highest = max(highest, int(line[l]+line[r]))
        res += highest
    print(res)
