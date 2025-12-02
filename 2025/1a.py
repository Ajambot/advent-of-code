cur = 50
res = 0
with open("1.txt") as f:
    for ins in f:
        dir = -1 if ins[0] == "L" else 1
        mag = int(ins[1:])
        cur = (cur + dir * mag) % 100
        if cur == 0:
            print(ins)
            res += 1
    print(res)
