import re
import math
f = open("17.txt", "r")

registers = []
for i in range(3):
    line = f.readline()
    registers.append(int(re.search(r"(\d+)", line).group(1)))
f.readline()

instructions = f.readline()[9:].split(",")
instructions = [int(c) for c in instructions]

def check(regA):
    ip = 0
    output = []
    regs = registers.copy()
    regs[0] = regA
    def getComboOperand(op):
        if 0 <= op <= 3:
            return op
        else:
            return regs[op-4]
    while ip < len(instructions):
        curI = instructions[ip]
        match curI:
            case 0:
                cOp = instructions[ip+1]
                num = regs[0]
                den = 2**getComboOperand(cOp)
                regs[0] = num // den
            case 1:
                a = regs[1]
                b = instructions[ip+1]
                regs[1] = a ^ b
            case 2:
                regs[1] = getComboOperand(instructions[ip+1]) % 8
            case 3:
                if regs[0]:
                    ip = instructions[ip+1]
                    continue
            case 4:
                a, b = regs[1], regs[2]
                regs[1] = a ^ b
            case 5:
                output.append(getComboOperand(instructions[ip+1])%8)
            case 6:
                cOp = instructions[ip+1]
                num = regs[0]
                den = 2**getComboOperand(cOp)
                regs[1] = num // den
            case 7:
                cOp = instructions[ip+1]
                num = regs[0]
                den = 2**getComboOperand(cOp)
                regs[2] = num // den
        ip += 2
    return instructions[len(instructions)-len(output):] == output

res = float("inf")
def dfs(num):
    global res
    if math.ceil(num.bit_length() / 3) == len(instructions):
        res = min(res, num)
        return
    for i in range(8):
        if num == 0 and i == 0:
            continue
        newNum = (num << 3) ^ (i)
        if check(newNum):
            dfs(newNum)
dfs(0)
print(res)
