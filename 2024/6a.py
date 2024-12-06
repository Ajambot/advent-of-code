f = open("6.txt")
map = []
for line in f:
    l = []
    for c in line:
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
while True:
    if map[i][o] != "X":
        count += 1
    map[i][o] = "X"
    l, r = dirs[dirI]
    if i+l < 0 or i+l >= n or o+r < 0 or o+r >= m:
        break
    if map[i+l][o+r] == "#":
        dirI = (dirI + 1) % 4
    l, r = dirs[dirI]
    if i+l < 0 or i+l >= n or o+r < 0 or o+r >= m:
        break
    i += l
    o += r

print(count)
