f = open("4.txt", "r")
grid = []
for line in f:
    grid.append(line.strip())

word = "XMAS"
n = len(grid)
m = len(grid[0])


def inBounds(i, o):
    return i >= 0 and i < n and o >= 0 and o < m

def xmas(i, o):
    dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for l, r in dirs:
        if not inBounds(i+l, o+r):
            return 0
    if (grid[i+1][o+1] == "M" and grid[i-1][o-1] == "S" or grid[i+1][o+1] == "S" and grid[i-1][o-1] == "M") and (grid[i+1][o-1] == "M" and grid[i-1][o+1] == "S" or grid[i+1][o-1] == "S" and grid[i-1][o+1] == "M"):
        return 1
    return 0

count = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
for i in range(n):
    for o in range(m):
        if grid[i][o] == "A":
            count += xmas(i, o)
print(count)
