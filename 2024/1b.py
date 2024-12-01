f = open("1.txt", "r")

count = {}
a = []
for line in f:
    l, r = line.split()
    a.append(int(l))
    count[int(r)] = count.get(int(r), 0) + 1 

res = 0
for num in a:
    res += num * (count[num] if num in count else 0)
print(res)
