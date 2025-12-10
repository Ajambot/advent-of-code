import math

def parseLights(lightsTxt):
    lightsExpected = ""
    for c in lightsTxt:
        if c in "[]":
            continue
        lightsExpected += "1" if c == "#" else "0"
    return lightsExpected

def parseButtons(buttonsTxt):
    buttons = []
    for bt in buttonsTxt:
        mask = "".join(["0" for _ in range(lightAmount)])
        bt = bt[1:-1]
        for p in bt.split(','):
            p = int(p)
            mask = mask[:p] + "1" + mask[p+1:]
            mask = int(mask)
            buttons.append(mask)
    return buttons

lightsExpected = 0
buttons = []
mem = {}

def dp(cur, pressed):
    if mem[cur] <= len(pressed):
        return
    mem[cur] = len(pressed)
    if cur == lightsExpected:
        return
    for i in range(len(buttons)):
        dp()

with open('10test.txt') as f:
    for line in f:
        line = line.strip()
        lightsTxt = line.split(' ')[0]
        buttonsTxt = line.split(' ')[1:-1]
        lightsExpected = parseLights(lightsTxt)

        lightAmount = len(lightsExpected)
        lightsExpected = int(lightsExpected)

        buttons = parseButtons(buttonsTxt)


