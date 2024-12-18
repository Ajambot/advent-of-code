import heapq
import re
f = open("18.txt", "r")

n = 71
grid = [["." for _ in range(n)] for _ in range(n)]

def runAStar():
    def h(x, y):
        return abs(n-1 - x) + (n-1 - y)
    pq = [(h(0,0), 0, 0)]

    dirs = [(0, 1), (1,0), (-1, 0), (0, -1)]
    vis = set()
    while pq:
        cur = heapq.heappop(pq)
        c, i, o = cur
        vis.add((i,o))
        g = c - h(i, o)
        if (i, o) == (n-1, n-1):
            return True

        for l, r in dirs:
            if min(i+l, o+r) >= 0 and max(i+l, o+r) < n and (i+l, o+r) not in vis and grid[i+l][o+r] == ".":
                heapq.heappush(pq, (g+1 + h(i+l, o+r), i+l, o+r))
                vis.add((i+l, o+r))
    return False

i = 0
while True:
    line = f.readline().strip()
    l, r = re.search(r"(\d+),(\d+)", line).group(1, 2)
    l, r = int(l), int(r)
    grid[l][r] = "#"
    if not runAStar():
        print(l, r)
        break
