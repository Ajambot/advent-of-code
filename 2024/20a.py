from collections import defaultdict

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
while True:
    i, o = cur
    grid[i][o] = steps
    steps += 1
    if cur == start:
        break
    for l, r in dirs:
        if grid[i+l][o+r] in [".", "S"]:
            cur = (i+l, o+r)

allDirs = [(2, 0), (0, 2), (-2, 0), (0, -2), (1,1), (-1, -1), (1, -1), (-1, 1)]
vis = set()
res = 0
n, m = len(grid), len(grid[0])
while start != end:
    vis.add(start)
    i, o = start
    for l, r in allDirs:
        if min(i+l, o+r) >= 0 and i+l < n and o+r < m and grid[i+l][o+r] != "#" and grid[i+l][o+r] < grid[i][o] and grid[i][o] - grid[i+l][o+r] - 2 >= 100:
            res += 1
    for l, r in dirs:
        if (i+l, o+r) not in vis and grid[i+l][o+r] != "#":
            start = (i+l, o+r)
print(res)
