import sys
import copy

sys.setrecursionlimit(5000)

def parseButtons(buttonsTxt):
    buttons:list[list[int]] = []
    for bt in buttonsTxt:
        cur = bt[1:-1].split(',')
        cur = [int(i) for i in cur]
        buttons.append(cur)
    return buttons

with open('10test.txt') as f:
    res = 0
    for line in f:
        mem = {}
        line = line.strip()
        buttonsTxt = line.split(' ')[1:-1]
        joltages = line.split(' ')[-1][1:-1].split(',')
        joltages = [int(j) for j in joltages]
        joltageAmount = len(joltages)

        buttons = parseButtons(buttonsTxt)
        mem = { tuple([0 for _ in range(joltageAmount)]): []}

        while True:
            change = False
            memCpy = copy.deepcopy(mem)
            for k, v in mem.items():
                for i, bt in enumerate(buttons):
                    cur = list(k)
                    exceeded = False
                    for index in bt:
                        cur[index] += 1
                        if cur[index] > joltages[index]:
                            exceeded = True
                    if exceeded:
                        continue

                    if tuple(cur) not in mem or len(mem[tuple(cur)]) > len(v)+1:
                        change = True
                        memCpy[tuple(cur)] = v + [i]
            if not change:
                break
            mem = memCpy

        print(mem[tuple(joltages)], len(mem[tuple(joltages)]))
        res += len(mem[tuple(joltages)])
    print(res)
