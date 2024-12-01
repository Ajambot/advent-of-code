f = open("1.txt", "r")

a, b = [], []
for line in f:
    l, r = line.split()
    a.append(int(l))
    b.append(int(r))

a.sort()
b.sort()

res = 0
for i in range(len(a)):
    res += abs(a[i]-b[i])
print(res)
