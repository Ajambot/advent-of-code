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

while l < r:
    while newS[l] != ".":
        l += 1
    while newS[r] == ".":
        r -= 1
    if not l < r:
        break

    newS[l] = newS[r]
    newS[r] = "."

i = 0
sum = 0
while newS[i] != ".":
    sum += i * int(newS[i])
    i += 1
print(sum)
