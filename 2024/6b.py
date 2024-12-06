f = open("6.txt")
map = []
for line in f:
    l = []
    for c in line.strip():
        l.append(c)
    map.append(l)


n = len(map)
m = len(map[0])
start = (0, 0)
for i in range(n):
    for o in range(m):
        if map[i][o] == "^":
            start = (i, o)

count = 0
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

i, o = start
dirI = 0
check = []
while i >= 0 and i < n and o >= 0 and o < m:
    l, r = dirs[dirI]
    if (i, o) != start:
        check.append((i,o))
    if i+l >= 0 and i+l < n and o+r >= 0 and o+r < m and map[i+l][o+r] == "#":
        dirI = (dirI + 1) % 4
        continue
    i += l
    o += r

def isLoop(i, o, dir):
    vis = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    while i >= 0 and i < n and o >= 0 and o < m:
        if vis[i][o][dir]:
            return True
        vis[i][o][dir] = True
        l, r = dirs[dir]
        if i+l >= 0 and i+l < n and o+r >= 0 and o+r < m and map[i+l][o+r] == "#":
            dir = (dir+1) % 4
            continue
        i += l
        o += r
    return False

cicleHere = set()
for l, r in check:
    temp = map[l][r]
    map[l][r] = "#"
    i, o = start
    if isLoop(i, o, 0):
        cicleHere.add((l, r))
    map[l][r] = temp

print(len(cicleHere))
