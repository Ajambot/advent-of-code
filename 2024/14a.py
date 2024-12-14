from collections import defaultdict
import re
f = open("14.txt", "r")

pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
position = []
velocity = []
for line in f:
    line = line.strip()
    test = re.search(pattern, line)
    px, py, vx, vy = re.search(pattern, line).group(1, 2, 3, 4)
    position.append([int(px), int(py)])
    velocity.append([int(vx), int(vy)])

newPs = defaultdict(int)

n, m = 101, 103
def printGrid(positions):
    for i in range(m):
        newLine = ""
        for o in range(n):
            if (o, i) in positions:
                newLine = newLine + str(positions[(o,i)])
            else:
                newLine += "."
        print(newLine)

for i, p in enumerate(position):
    px, py = p
    vx, vy = velocity[i]
    newPx = ((px + vx * 100) % n)
    newPy = ((py + vy * 100) % m)
    newP = (newPx, newPy)
    newPs[newP] += 1

res = 0
q1 = q2 = q3 = q4 = 0
for p in newPs:
    px, py = p
    if px < n//2 and py < m//2:
        q1 += newPs[p]
    elif px > n//2 and py < m//2:
        q2 += newPs[p]
    elif px < n//2 and py > m//2:
        q3 += newPs[p]
    elif px > n//2 and py > m//2:
        q4 += newPs[p]
print(q1*q2*q3*q4)
