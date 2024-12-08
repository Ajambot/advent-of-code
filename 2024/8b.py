from collections import defaultdict
f = open("8.txt")
grid = []
for line in f:
    line = [c for c in line.strip()]
    grid.append(line)

antMap = defaultdict(list)
n = len(grid)
m = len(grid[0])
for i in range(n):
    for o in range(m):
        if grid[i][o] != ".":
            antMap[grid[i][o]].append((i, o))

antinodes = set()
for key in antMap:
    positions = antMap[key]
    for i in range(len(positions)):
        for o in range(i+1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[o]
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))
            diffX = x1-x2
            diffY = y1-y2
            j = 1
            while x1 + diffX*j >= 0 and x1 + diffX*j < n and y1 + diffY*j >= 0 and y1 + diffY*j < m:
                antinodes.add((x1+diffX*j, y1+diffY*j))
                j += 1
            diffX = x2-x1
            diffY = y2-y1
            j = 1
            while x2 + diffX*j >= 0 and x2 + diffX*j < n and y2 + diffY*j >= 0 and y2 + diffY*j < m:
                antinodes.add((x2+diffX*j, y2+diffY*j))
                j += 1
print(len(antinodes))
