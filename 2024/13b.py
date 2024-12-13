import numpy as np
import re
f = open("13.txt", "r")
def is_close_to_whole_number(x, tolerance = 1e-4):
    return abs(x-round(x)) < tolerance
res = 0
while True:
    a = f.readline()
    b = f.readline()
    target = f.readline()
    buttonPattern = 'X\+(\d+), Y\+(\d+)'
    a = re.search(buttonPattern, a)
    b = re.search(buttonPattern, b)
    ax, ay = a.group(1, 2)
    bx, by = b.group(1, 2)

    targetPattern = 'X=(\d+), Y=(\d+)'
    target = re.search(targetPattern, target)
    targetx, targety = target.group(1, 2)
    ax, ay, bx, by, targetx, targety = int(ax), int(ay), int(bx), int(by), int(targetx), int(targety)
    targetx = targetx + 10000000000000
    targety = targety + 10000000000000
    A = np.matrix([[ax, bx], [ay, by]])
    B = np.matrix([[targetx], [targety]])
    X = np.linalg.solve(A, B)
    X = X.tolist()
    if is_close_to_whole_number(X[0][0]) and is_close_to_whole_number(X[1][0]):
        res += round(X[0][0]) * 3 + round(X[1][0])
    if f.readline() == '':
        break
print(res)
