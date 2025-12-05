with open('5.txt') as f:
    ranges = []
    while True:
        line = f.readline().strip()
        if len(line) < 1:
            break
        ranges.append(line)

    ids = []
    while True:
        line = f.readline().strip()
        if len(line) == 0:
            break
        ids.append(int(line))

    freshCount = 0
    for id in ids:
        for rangeNum in ranges:
            lrange = rangeNum.split('-')[0]
            rrange = rangeNum.split('-')[1]
            if id >= int(lrange) and id <= int(rrange):
                freshCount += 1
                break
    print(freshCount)
