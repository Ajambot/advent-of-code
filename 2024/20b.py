f = open("20.txt", "r")

i = 0
grid = []
start = (-1, -1)
end = (-1, -1)
for line in f:
    newLine = []
    o = 0
    for c in line.strip():
        newLine.append(c)
        if c == "S":
            start = (i, o)
        if c == "E":
            end = (i, o)
        o += 1
    grid.append(newLine)
    i += 1

dirs = [(0, 1), (1,0), (-1, 0), (0, -1)]

cur = end
steps = 0
path = []
while True:
    i, o = cur
    grid[i][o] = "O"
    path.append((i, o, steps))
    steps += 1
    if cur == start:
        break
    for l, r in dirs:
        if grid[i+l][o+r] in [".", "S"]:
            cur = (i+l, o+r)

res = 0
save ={}
for i in range(len(path)):
    for o in range(i+1, len(path)):
        x1, y1, s1 = path[i]
        x2, y2, s2 = path[o]
        if s2 > s1:
            x1, y1, s1, x2, y2, s2 = x2, y2, s2, x1, y1, s1
        dist = abs(x1-x2) + abs(y1-y2)
        if dist <= 20 and s1-s2-dist >= 100:
            res += 1
            save[s1-s2-dist] = save.get(s1-s2-dist, 0) + 1
print(res)
