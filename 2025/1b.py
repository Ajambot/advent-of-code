cur = 50
res = 0
with open("1.txt") as f:
    for ins in f:
        dir = -1 if ins[0] == "L" else 1
        mag = int(ins[1:])
        if dir == 1:
            while mag > 0:
                minN = min(100-cur, mag)
                cur = (cur + minN)%100
                mag -= minN
                if cur == 0:
                    res += 1
        else:
            while mag > 0:
                if cur == 0:
                    minN = min(100, mag)
                else:
                    minN = min(cur, mag)
                cur = (cur - minN)%100
                mag -= minN
                if cur == 0:
                    res += 1
    print(res)
