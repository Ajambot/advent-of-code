f = open("12.txt", "r")

farm = []
for line in f:
    newLine = []
    for c in line.strip():
        newLine.append(c)
    farm.append(newLine)

n, m = len(farm), len(farm[0])
vis = set()
perimeter = 0
area = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(i, o):
    global perimeter, area
    if (i, o) in vis:
        return
    
    area += 1
    vis.add((i, o))
    for l, r in dirs:
        if min(i+l, o+r) < 0 or i+l >= n or o+r >= m or farm[i+l][o+r] != farm[i][o]:
            perimeter += 1
        else:
            dfs(i+l, o+r)

res = 0
for i in range(n):
    for o in range(m):
        perimeter = area = 0
        dfs(i, o)
        res += perimeter * area
print(res)
