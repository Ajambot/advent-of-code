def checkValid(points, i, o):
    c1x, c1y = points[i]
    c2x, c2y = points[o]
    # lu corner case
    if c1x <= c2x and c1y <= c2y:
        cur = i+1
        curx, cury = points[cur%len(points)]
        while cur%len(points) != o:
            if (c1x < curx < c2x) and (c1y < cury < c2y):
                return False
            prevx, prevy = points[(cur-1)%len(points)]
            if ((prevx <= c1x and curx >= c2x) or (prevx >= c2x and curx <= c1x)) and (c1y < cury < c2y):
                return False
            if ((prevy <= c1y and cury >= c2y) or (prevy >= c2y and cury <= c1y)) and (c1x < curx < c2x):
                return False
            cur += 1
            curx, cury = points[cur%len(points)]
    # ru corner case
    elif c1x >= c2x and c1y <= c2y:
        cur = i+1
        curx, cury = points[cur%len(points)]
        while cur%len(points) != o:
            if (c2x < curx < c1x) and (c1y < cury < c2y):
                return False
            prevx, prevy = points[(cur-1)%len(points)]
            if ((prevx >= c1x and curx <= c2x) or (prevx <= c2x and curx >= c1x)) and (c1y < cury < c2y):
                return False
            if ((prevy <= c1y and cury >= c2y) or (prevy >= c2y and cury <= c1y)) and (c2x < curx < c1x):
                return False
            cur += 1
            curx, cury = points[cur%len(points)]
    # rd corner case
    elif c1x >= c2x and c1y >= c2y:
        cur = i+1
        curx, cury = points[cur%len(points)]
        while cur%len(points) != o:
            if (c2x < curx < c1x) and (c2y < cury < c1y):
                return False
            prevx, prevy = points[(cur-1)%len(points)]
            if ((prevx >= c1x and curx <= c2x) or (prevx <= c2x and curx >= c1x)) and (c2y < cury < c1y):
                return False
            if ((prevy >= c1y and cury <= c2y) or (prevy <= c2y and cury >= c1y)) and (c2x < curx < c1x):
                return False
            cur += 1
            curx, cury = points[cur%len(points)]

    # ld corner case
    elif c1x <= c2x and c1y >= c2y:
        cur = i+1
        curx, cury = points[cur%len(points)]
        while cur%len(points) != o:
            if (c1x < curx < c2x) and (c2y < cury < c1y):
                return False
            prevx, prevy = points[(cur-1)%len(points)]
            if ((prevx <= c1x and curx >= c2x) or (prevx >= c2x and curx <= c1x)) and (c2y < cury < c1y):
                return False
            if ((prevy >= c1y and cury <= c2y) or (prevy <= c2y and cury >= c1y)) and (c1x < curx < c2x):
                return False
            cur += 1
            curx, cury = points[cur%len(points)]
    return True


with open('9.txt') as f:
    points = []
    for line in f:
        x, y = line.strip().split(',')
        points.append((int(x), int(y)))

    maxA = 0
    for i in range(len(points)):
        for o in range(i+1, len(points)):
            c1x, c1y = points[i]
            c2x, c2y = points[o]
            area = (abs(c1x-c2x)+1) * (abs(c1y-c2y)+1)
            if checkValid(points, i, o) and checkValid(points, o, i):
                maxA = max(maxA, area)

    print(maxA)
