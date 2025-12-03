import re
f = open("21.txt", "r")

keypad = { "7": (0, 0),
           "8": (0, 1),
           "9": (0, 2),
           "4": (1, 0),
           "5": (1, 1),
           "6": (1, 2),
           "1": (2, 0),
           "2": (2, 1),
           "3": (2, 2),
           "0": (3, 1),
           "A": (3, 2),
          }

possible = []
def dirToNumpad(origin, target, cur):
    x, y = origin
    if not (0 <= x <= 3 and 0 <= y <= 2):
        return
    if origin == (3, 0):
        return
    if len(cur) > 10:
        return
    if origin == target:
        possible.append(cur)
        return

    dirToNumpad((x+1, y), target, cur + "v")
    dirToNumpad((x-1, y), target, cur + "v")
    dirToNumpad((x, y+1), target, cur + ">")
    dirToNumpad((x, y-1), target, cur + "<")

dirPad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

def dirToDirpad(origin, target, cur):
    x, y = origin
    if not (0 <= x <= 1 and 0 <= y <= 2):
        return
    if origin == (0, 0):
        return
    if len(cur) > 4:
        return
    if origin == target:
        possible.append(cur)
        return

    dirToDirpad((x+1, y), target, cur + "v")
    dirToDirpad((x-1, y), target, cur + "v")
    dirToDirpad((x, y+1), target, cur + ">")
    dirToDirpad((x, y-1), target, cur + "<")

res = 0
for line in f:
    code = line.strip()
    num = int(re.search(r"(\d+)", line).group(1))
    numPadDirs = ""
    last = "A"
    for c in code:
        numPadDirs += dirToNumpad(last, c)
        numPadDirs += "A"
        last = c
    #print(numPadDirs, len(numPadDirs))

    dirPadDirs = ""
    last = "A"
    for c in numPadDirs:
        dirPadDirs += dirToDirpad(last, c)
        dirPadDirs += "A"
        last = c
    #print(dirPadDirs, len(dirPadDirs))

    last = "A"
    newDirPadDirs = ""
    for c in dirPadDirs:
        newDirPadDirs += dirToDirpad(last, c)
        newDirPadDirs += "A"
        last = c
    print(code, newDirPadDirs, len(newDirPadDirs))
    res += len(newDirPadDirs) * num
# 193380 too high
print(res)
