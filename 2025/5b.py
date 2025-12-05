def mergeRanges(ranges:list[list]):
    ranges.sort()
    finalRanges = [ranges[0]]

    for l, r in ranges[1:]:
        if l <= finalRanges[-1][1]:
            finalRanges[-1][1] = max(finalRanges[-1][1], r)
        else:
            finalRanges.append([l, r])
    return finalRanges


with open('5.txt') as f:
    ranges = []
    while True:
        line = f.readline().strip()
        if len(line) < 1:
            break
        lrange = line.split('-')[0]
        rrange = line.split('-')[1]
        ranges.append([int(lrange), int(rrange)])
    merged = mergeRanges(ranges)
    res = 0
    for l, r in merged:
        res += r - l + 1
    print(res)
