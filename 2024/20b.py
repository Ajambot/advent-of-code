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
path = {}
while True:
    i, o = cur
    grid[i][o] = "O"
    path[(i, o)] = steps
    steps += 1
    if cur == start:
        break
    for l, r in dirs:
        if grid[i+l][o+r] in [".", "S"]:
            cur = (i+l, o+r)

res = 0
for coord in path:
    x, y = coord
    dist = path[coord]
    for i in range(21):
        for o in range(21):
            if i == 0 and o == 0:
                continue
            if i+o > 20:
                continue
            if (x+i, y+o) in path and dist - path[(x+i, y+o)] - (i+o) >= 100:
                res += 1

            if i and (x-i, y+o) in path and dist - path[(x-i, y+o)] - (i+o) >= 100:
                res += 1

            if o and (x+i, y-o) in path and dist - path[(x+i, y-o)] - (i+o) >= 100:
                res += 1

            if i and o and (x-i, y-o) in path and dist - path[(x-i, y-o)] - (i+o) >= 100:
                res += 1
print(res)
