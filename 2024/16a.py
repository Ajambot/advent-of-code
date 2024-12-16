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

hp = [(0 + h(start, 0), start, 0)]

vis = set()
while hp:
    c, p, d = heapq.heappop(hp)
    #print(c, p, d)
    if p == end:
        print(c)
        break

    vis.add((p, d))
    newP = tuple([sum(x) for x in zip(p, dirs[d])])
    newI, newO = newP
    g = c - h(p, d)
    if (newP, d) not in vis and maze[newI][newO] in ["E", "."]:
        heapq.heappush(hp, (1+g+h(newP, d), newP, d))

    clockwise = (d+1)%4
    cclockwise = (d-1)%4

    for dir in [clockwise, cclockwise]:
        if (p, dir) not in vis:
            heapq.heappush(hp, (1000+g+h(p, dir), p, dir))
