import sys

sys.setrecursionlimit(5000)

def parseLights(lightsTxt, length):
    lightsExpected = 0
    for c in lightsTxt:
        if c in "[]":
            continue
        if c == "#":
            lightsExpected |= 1<<(length-1)
        length -= 1
    return lightsExpected

def parseButtons(buttonsTxt, length):
    buttons = []
    for bt in buttonsTxt:
        mask = 0
        bt = bt[1:-1]
        for p in bt.split(','):
            mask |= 1<<(length-int(p)-1)
        buttons.append(mask)
    return buttons

lightsExpected = 0
buttons = []
mem = {}

def dp(cur, pressed):
    if cur in mem and len(mem[cur]) <= len(pressed):
        return
    mem[cur] = pressed
    if cur == lightsExpected:
        return
    for i in range(len(buttons)):
        dp(cur ^ buttons[i], pressed + [i])

with open('10test.txt') as f:
    res = 0
    for line in f:
        mem = {}
        line = line.strip()
        lightsTxt = line.split(' ')[0]
        buttonsTxt = line.split(' ')[1:-1]
        lightAmount = len(lightsTxt)-2
        lightsExpected = parseLights(lightsTxt, lightAmount)

        lightsExpected = int(lightsExpected)

        buttons = parseButtons(buttonsTxt, lightAmount)
        # print("Expected: ", bin(lightsExpected))
        # for bt in buttons:
        #     print(bin(bt))
        dp(0, [])
        print(len(mem[lightsExpected]), mem[lightsExpected])
        res += len(mem[lightsExpected])
    print(res)
