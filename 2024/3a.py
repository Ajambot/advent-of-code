f = open("3.txt", "r")
def readNum(i, s):
    j = 0
    while i+j < len(s) and s[i+j] in "0123456789" and j <= 3:
        j += 1
    if j <= 3 and i+j < len(s):
        return i+j
    return -1

res = 0
stream = f.read()
i = 0
while i < len(stream):
    i = stream.find("(", i)
    l = i
    if i == -1:
        break
    if i >= 3 and stream[i-3:i] == "mul":
        j = readNum(i+1, stream)
        if j == -1 or stream[j] != ",":
            i += 1
            continue
        n1 = stream[i+1:j]
        i = j
        j = readNum(j+1, stream)
        if j == -1 or stream[j] != ")":
            i += 1
            continue
        n2 = stream[i+1:j]
        res += int(n1) * int(n2)
        i = j
        r = i
    i += 1

print(res)
f.close()
