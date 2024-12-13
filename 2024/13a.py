import re
f = open("13.txt", "r")

res = 0
while True:
    a = f.readline()
    b = f.readline()
    target = f.readline()
    buttonPattern = 'X\+(\d+), Y\+(\d+)'
    a = re.search(buttonPattern, a)
    b = re.search(buttonPattern, b)
    ax, ay = a.group(1, 2)
    bx, by = b.group(1, 2)

    targetPattern = 'X=(\d+), Y=(\d+)'
    target = re.search(targetPattern, target)
    targetx, targety = target.group(1, 2)
    ax, ay, bx, by, targetx, targety = int(ax), int(ay), int(bx), int(by), int(targetx), int(targety)

    q = [(ax, ay, 3), (bx, by, 1)]
    mem = {}
    while q:
        x, y, cost = q.pop()
        if (x, y) not in mem or mem[(x, y)] > cost:
            mem[(x, y)] = cost
            if x >= targetx or y >= targety:
                continue
            q.append((x+ax, y+ay, cost+3))
            q.append((x+bx, y+by, cost+1))
    if (targetx, targety) in mem:
        res += mem[(targetx, targety)]
    if f.readline() == '':
        break
print(res)
