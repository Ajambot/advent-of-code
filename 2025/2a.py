with open('2.txt') as f:
    line = f.readline()
    ranges = line.split(',')
    res = 0
    for i in range(2, 11, 2):
        l = 10 ** (i//2 - 1)
        r = 10 ** (i//2)
        for x in range(l, r):
            num = int(str(x) + str(x))
            for rangeNum in ranges:
                lrange = rangeNum.split('-')[0]
                rrange = rangeNum.split('-')[1]
                if num >= int(lrange) and num <= int(rrange):
                    print(num)
                    res += num
    print(res)
