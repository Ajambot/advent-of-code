f = open("10.txt", "r")

mp = []
for line in f:
    mp.append(line.strip())

count = 0

n, m = len(mp), len(mp[0])

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dfs(i, o):
    if int(mp[i][o]) == 9:
        return 1

    paths = 0
    for l, r in dirs:
        if min(i+l, o+r) >= 0 and i+l < n and o+r < m and int(mp[i+l][o+r]) == int(mp[i][o])+1: 
            paths += dfs(i+l, o+r)
    return paths

count = 0
for i in range(n):
    for o in range(m):
        if mp[i][o] == "0":
            count += dfs(i, o)
print(count)
