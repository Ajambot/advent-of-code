import heapq

f = open("16.txt")

maze = []
i = 0
start = end = (-1, -1)
for line in f:
    newL = []
    o = 0 
    for c in line.strip():
        if c == "S":
            start = (i, o)
        if c == "E":
            end = (i, o)
        newL.append(c)
        o += 1
    maze.append(newL)
    i += 1

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

# Heuristic function (estimate of cost)
# Best score would be to take the path of the manhattan distance, since we minimize our turns and our distance
# We also have to take the direction into account. If we are not facing a way that gets us closer to the end,
# we will have to turn. If we are not in the same row or column as the end, we will also have to turn
def h(n, d):
    cost = 0
    dir = dirs[d]
    if n == end:
        return 0
    if abs(end[0] - n[0] + dir[0]) > abs(end[0] - n[0]) or abs(end[1] - n[1] + dir[1]) > abs(end[1] - n[1]):
        cost += 1000
    if n[0] != end[0] and n[1] != end[1]:
        cost += 1000
    return cost + abs(end[0] - n[0]) + abs(end[1] - n[1])

path = set()
path.add(start)
hp = [(0 + h(start, 0), start, 0, path)]

vis = {}
bestPaths = set()
while hp:
    c, p, d, path = heapq.heappop(hp)
    if p == end:
        for i in range(4):
            vis[(p, i)] = c
        bestPaths = bestPaths.union(path)
        continue

    vis[(p, d)] = c
    newP = tuple([sum(x) for x in zip(p, dirs[d])])
    newI, newO = newP
    g = c - h(p, d)
    if ((newP, d) not in vis or vis[(newP, d)] >= 1+g+h(newP, d)) and maze[newI][newO] in ["E", "."]:
        newPath = path.copy()
        newPath.add(newP)
        heapq.heappush(hp, (1+g+h(newP, d), newP, d, newPath))

    clockwise = (d+1)%4
    cclockwise = (d-1)%4

    for dir in [clockwise, cclockwise]:
        if (p, dir) not in vis or vis[(p, dir)] >= 1000+g+h(p, dir):
            heapq.heappush(hp, (1000+g+h(p, dir), p, dir, path))
print(len(bestPaths))
