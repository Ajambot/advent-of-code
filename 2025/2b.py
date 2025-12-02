with open('2.txt') as f:
    line = f.readline()
    ranges = line.split(',')
    res = 0
    done = set()
    for rangeNums in ranges:
        lrange = rangeNums.split('-')[0]
        rrange = rangeNums.split('-')[1]
        for x in range(int(lrange), int(rrange)+1):
            lenX = len(str(x))
            for length in range(1, lenX//2+1):
                if lenX % length != 0 or lenX / length < 2:
                    continue
                pattern = str(x)[:length]
                possible = True
                for y in range(length, lenX, length):
                    if str(x)[y:y+length] != pattern:
                        possible = False
                        break
                if possible and x not in done:
                    done.add(x)
                    res += x

    print(res)
