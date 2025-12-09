with open('9.txt') as f:
    points = []
    for line in f:
        x, y = line.strip().split(',')
        points.append((int(x), int(y)))

    maxA = 0
    for i in range(len(points)):
        for o in range(i, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[o]
            area = (abs(x2-x1)+1) * (abs(y2-y1)+1)
            maxA = max(maxA, area)
    print(maxA)
