f = open("3.txt", "r")
def readNum(i, s):
    j = 0
    while i+j < len(s) and s[i+j] in "0123456789" and j <= 3:
        j += 1
    if j <= 3 and i+j < len(s):
        return i+j
    return -1

stream = f.read()
res = 0
i = 0
dont = stream.find("don't()")
if dont == -1:
    dont = len(stream)
while i < len(stream):
    i = stream.find("(", i)
    if i == -1:
        break
    if i < dont:
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
    else:
        i = stream.find("do()", i)
        if i == -1:
            break
        dont = stream.find("don't()", i)
        if dont == -1: dont = len(stream)
    i += 1

print("res", res)
f.close()
