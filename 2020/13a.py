f = open("practice.txt")

i = 0
n = -1
buses = []
for line in f:
    if i == 0:
        n = int(line.strip())
    else:
        buses = line.strip().split(",")
    i += 1

minMins = [1, float("inf")]
for bus in buses:
    if bus == "x":
        continue
    bus = int(bus)
    if n % bus == 0:
        minMins = 0
        break
    div = n // bus + 1
    rem = (bus * div) - n
    print(bus, div, rem)
    if rem < minMins[1]:
        minMins = [bus, rem]

print(minMins[0], minMins[1])
print(minMins[0]*minMins[1])
