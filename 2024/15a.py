f = open("15.txt", "r")
grid = []
i = o = 0
start = (-1, -1)
for line in f:
    if line == "\n":
        break
    newLine = []
    o = 0
    for c in line.strip():
        if c == "@":
            start = (i, o)
        newLine.append(c)
        o += 1
    grid.append(newLine)
    i += 1

instructions = f.read().replace("\n", "")

dirs = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

n =  len(grid)
m = len(grid[0])

def propagate(p, d):
    i, o = p
    newP = [sum(x) for x in zip (p, d)]
    newI, newO = newP
    if grid[newI][newO] == '.':
        grid[newI][newO] = grid[i][o]
        grid[i][o] = "."
        return True
    if grid[newI][newO] == "#":
        return False
    if propagate(newP, d):
        grid[newI][newO] = grid[i][o]
        grid[i][o] = "."
        return True
    return False

for ins in instructions:
    dir = dirs[ins]
    if propagate(start, dir):
        start = [sum(x) for x in zip(start, dir)]
    #for row in grid:
    #    print("".join(row))
    #print()

def GPSSum():
    sum = 0
    for i in range(n):
        for o in range(m):
            if grid[i][o] == "O":
                sum += (100 * i + o)
    return sum

print(GPSSum())
