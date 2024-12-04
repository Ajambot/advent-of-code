f = open("4.txt", "r")
grid = []
for line in f:
    grid.append(line.strip())

word = "XMAS"
n = len(grid)
m = len(grid[0])


def inBounds(i, o):
    return i >= 0 and i < n and o >= 0 and o < m

def dfs(i, o, wi, dirs):
    if wi == len(word):
        return 1
    if not inBounds(i, o) or grid[i][o] != word[wi]:
        return 0
    count = 0
    for dir in dirs:
        l, r = dir
        count += dfs(i+l, o+r, wi+1, [dir])
    return count

count = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
for i in range(n):
    for o in range(m):
        if grid[i][o] == "X":
            count += dfs(i, o, 0, dirs)
print(count)
