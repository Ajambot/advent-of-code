f = open("12test.txt", "r")

farm = []
for line in f:
    newLine = []
    for c in line.strip():
        newLine.append(c)
    farm.append(newLine)

n, m = len(farm), len(farm[0])
vis = set()
sideVis = set()
sides = 0
area = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def inBounds(i,  o):
    return min(i, o) >= 0 and i < n and o < m

def dfs(i, o):
    global sides, area
    if (i, o) in vis:
        return
    
    area += 1
    vis.add((i, o))
    for l, r in dirs:
        if (not inBounds(i+l, o+r) or farm[i+l][o+r] != farm[i][o]) and (i, o, l, r) not in sideVis:
            crop = farm[i][o]
            if l:
                j = 1
                while inBounds(i, o+j) and farm[i][o+j] == crop and (not inBounds(i+l, o+j) or farm[i+l][o+j] != farm[i][o+j]):
                    sideVis.add((i, o+j, l, r))
                    j += 1
                j = -1
                while inBounds(i, o+j) and farm[i][o+j] == crop and (not inBounds(i+l, o+j) or farm[i+l][o+j] != farm[i][o+j]):
                    sideVis.add((i, o+j, l, r))
                    j -= 1
                sides += 1
            elif r:
                j = 1
                while inBounds(i+j, o) and farm[i+j][o] == crop and (not inBounds(i+j, o+r) or farm[i+j][o+r] != crop):
                    sideVis.add((i+j, o, l, r))
                    j += 1
                j = -1
                while inBounds(i+j, o) and farm[i+j][o] == crop and (not inBounds(i+j, o+r) or farm[i+j][o+r] != crop):
                    sideVis.add((i+j, o, l, r))
                    j -= 1
                sides += 1
        else:
            if inBounds(i+l, o+r) and farm[i+l][o+r] == farm[i][o]:
                dfs(i+l, o+r)

res = 0
for i in range(n):
    for o in range(m):
        sides = area = 0
        sideVis = set()
        dfs(i, o)
        res += sides * area
print(res)
