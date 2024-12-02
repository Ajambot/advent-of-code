f = open("2.txt", "r")

def checkList(list):
    ascending = int(list[0]) < int(list[1])
    for i in range(len(list)-1):
        diff = abs(int(list[i])-int(list[i+1]))
        if diff < 1 or diff > 3:
            return False
        if ascending and int(list[i]) > int(list[i+1]):
            return False
        if (not ascending) and int(list[i]) < int(list[i+1]):
            return False
    return True

sum = 0
for line in f:
    report = line.split()
    check = checkList(report) 
    if check:
        sum += 1
print(sum)
