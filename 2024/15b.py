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
            newLine.append(c)
            newLine.append(".")
        if c == "O":
            newLine.append('[')
            newLine.append("]")
        if c == ".":
            newLine.append('.')
            newLine.append(".")
        if c == "#":
            newLine.append('#')
            newLine.append("#")
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
for i in range(n):
    for o in range(m):
        if grid[i][o] == "@":
            start = (i, o)

def check(p, d):
    newP = [sum(x) for x in zip (p, d)]
    newI, newO = newP
    if grid[newI][newO] == "#" or grid[newI][newO+1] == '#':
        return False
    if grid[newI][newO-1] == "[":
        if not check((newI, newO-1), d):
            return False
    if grid[newI][newO] == "[":
        if not check((newI, newO), d):
            return False
    if grid[newI][newO+1] == "[":
        if not check((newI, newO+1), d):
            return False
    return True

def propagateVertical(p, d):
    i, o = p
    newP = [sum(x) for x in zip (p, d)]
    newI, newO = newP
    if grid[newI][newO-1] == "[":
        propagateVertical((newI, newO-1), d)
    if grid[newI][newO] == "[":
        propagateVertical((newI, newO), d)
    if grid[newI][newO+1] == "[":
        propagateVertical((newI, newO+1), d)
    grid[newI][newO] = "["
    grid[newI][newO+1] = "]"
    grid[i][o] = "."
    grid[i][o+1] = "."

def propagateHorizontal(p, d):
    i, o = p
    newP = [sum(x) for x in zip (p, d)]
    newI, newO = newP
    if grid[newI][newO] == '.':
        grid[newI][newO] = grid[i][o]
        grid[i][o] = "."
        return True
    if grid[newI][newO] == "#":
        return False
    if propagateHorizontal(newP, d):
        grid[newI][newO] = grid[i][o]
        grid[i][o] = "."
        return True
    return False

for ins in instructions:
    dir = dirs[ins]
    if ins in ["<", ">"]:
        if propagateHorizontal(start, dir):
            start = [sum(x) for x in zip(start, dir)]
    else:
        newP = [sum(x) for x in zip (start, dir)]
        i, o = start
        newI, newO = newP
        if grid[newI][newO] == "#":
            continue
        elif grid[newI][newO] == ".":
            grid[newI][newO] = "@"
            grid[i][o] = "."
            start = newP
        else:
            if grid[newI][newO] == "[":
                if check((newI, newO), dir):
                    propagateVertical((newI, newO), dir)
                    start = [sum(x) for x in zip(start, dir)]
                    grid[newI][newO] = "@"
                    grid[i][o] = "."
                    start = newP
            elif grid[newI][newO-1] == "[":
                if check((newI, newO-1), dir):
                    propagateVertical((newI, newO-1), dir)
                    start = [sum(x) for x in zip(start, dir)]
                    grid[newI][newO] = "@"
                    grid[i][o] = "."
                    start = newP

def GPSSum():
    sum = 0
    for i in range(n):
        for o in range(m):
            if grid[i][o] == "[":
                sum += (100 * i + o)
    return sum

print(GPSSum())
