f = open("9.txt", "r")

s = f.read().strip()
newS = []

n = len(s)
id = 0
for i in range(0, n, 2):
    l = int(s[i])

    for j in range(l):
        newS.append(str(id))
    if i+1 >= len(s):
        break
    r = int(s[i+1])
    for j in range(r):
        newS.append(".")
    id += 1

l = 0
r = len(newS) - 1

spaces = []

l = 0
while l < len(newS):
    if newS[l] == ".":
        r = l
        while r+1 < len(newS) and newS[r+1] == ".":
            r += 1
        spaces.append([l, r-l+1])
        l = r
    l += 1

r = len(newS) - 1
while r > 0:
    while newS[r] == ".":
        r -= 1
    k = r
    id = newS[r]
    while k-1 >= 0 and newS[k-1] == id:
        k -= 1

    fileLen = r - k + 1
    for index, spaceInfo in enumerate(spaces):
        i, l = spaceInfo
        if i >= k:
            break
        elif l < fileLen:
            continue
        else:
            j = k
            while j <= r:
                newS[i] = newS[j]
                newS[j] = "."
                j += 1
                i += 1
            if l - fileLen:
                spaces[index][0] += fileLen
                spaces[index][1] -= fileLen
            else:
                del spaces[index]
            break
    r = k - 1

sum = 0
for i, c in enumerate(newS):
    if c == ".":
        continue
    sum += i * int(c)
print(sum)
