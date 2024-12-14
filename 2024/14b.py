from collections import defaultdict
import os
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

# These are the positions where I saw patterns that could resemble a christmas tree in a future repetition
# c1 is the first position of a horizontal pattern and c2 is the position of a vertical pattern
# Similar patterns repeated every 103 and 101 steps respectively (i.e. the width and height of the grid)
# Therefore, check every repetition of those patterns until you see a christmas tree
# For my input, the christmas tree happened when the horizontal pattern and the vertical pattern coincide at 7338
c1, c2 = 25, 66
while True:
    os.system('cls')
    newPs = defaultdict(int)
    for i, p in enumerate(position):
        px, py = p
        vx, vy = velocity[i]
        newPx = ((px + vx * c1) % n)
        newPy = ((py + vy * c1) % m)
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
    print(c1)
    printGrid(newPs)

    newPs = defaultdict(int)
    for i, p in enumerate(position):
        px, py = p
        vx, vy = velocity[i]
        newPx = ((px + vx * c2) % n)
        newPy = ((py + vy * c2) % m)
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

    print()
    print(c2)
    printGrid(newPs)
    t = input()
    if "b" in t:
        c1 -= 103
        c2 -= 101
    else:
        c1 += 103
        c2 += 101
