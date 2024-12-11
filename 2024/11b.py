from collections import defaultdict
from typing import Counter


f = open("11.txt", "r")

s = f.read().strip()

stones = s.split()
stones = [int(stone) for stone in stones]
counts = Counter(stones)

for i in range(75):
    newCounts = defaultdict(int)
    newCounts[1] += counts[0]
    for count in counts:
        if count == 0:
            continue
        if len(str(count)) % 2 == 0:
            m = len(str(count))//2
            l, r = int(str(count)[0:m]), int(str(count)[m:])
            newCounts[l] += counts[count]
            newCounts[r] += counts[count]
        else:
            newCounts[count*2024] += counts[count]
    counts = newCounts

res = 0
for count in counts:
    res += counts[count]

print(res)
