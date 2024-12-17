import re
f = open("17.txt", "r")

registers = []
for i in range(3):
    line = f.readline()
    registers.append(int(re.search(r"(\d+)", line).group(1)))
f.readline()

instructions = f.readline()[9:].split(",")
instructions = [int(c) for c in instructions]

def getComboOperand(op):
    if 0 <= op <= 3:
        return op
    else:
        return registers[op-4]

ip = 0
output = []
while ip < len(instructions):
    curI = instructions[ip]
    match curI:
        case 0:
            cOp = instructions[ip+1]
            num = registers[0]
            den = 2**getComboOperand(cOp)
            registers[0] = num // den
        case 1:
            a = registers[1]
            b = instructions[ip+1]
            registers[1] = a ^ b
        case 2:
            registers[1] = getComboOperand(instructions[ip+1]) % 8
        case 3:
            if registers[0]:
                ip = instructions[ip+1]
                continue
        case 4:
            a, b = registers[1], registers[2]
            registers[1] = a ^ b
        case 5:
            output.append(getComboOperand(instructions[ip+1])%8)
        case 6:
            cOp = instructions[ip+1]
            num = registers[0]
            den = 2**getComboOperand(cOp)
            registers[1] = num // den
        case 7:
            cOp = instructions[ip+1]
            num = registers[0]
            den = 2**getComboOperand(cOp)
            registers[2] = num // den
    ip += 2

output = [str(x) for x in output]
print(",".join(output))
