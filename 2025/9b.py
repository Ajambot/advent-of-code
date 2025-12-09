with open('9test.txt') as f:
    points = []
    for line in f:
        x, y = line.strip().split(',')
        points.append((int(x), int(y)))

    maxA = 0
    dirx = 0
    diry = 0
    st = [(points[0][0], points[0][1])]
    for i in range(1, len(points)*2):
        x, y = points[i%len(points)]
        if dirx == 0 and st[-1][0] != x: 
                dirx = 1 if x > st[-1][0] else -1
                st.append((x, st[-1][1]))
        elif diry == 0 and st[-1] != y: 
                diry = 1 if y > st[-1][1] else -1
                st.append((st[-1][0], y))

        if (dirx > 0 and x > st[-1][0]) or (dirx < 0  and x < st[-1][0]):
            st.append((x, st[-1][1]))
        else:
            if dirx > 0:
                corner = st.pop()
                while st and st[-1][0] > x:
                    area = (abs(corner[0]-st[-1][0]) + 1) * (abs(corner[1]-st[-1][1]) + 1)
                    st.pop()
                    maxA = max(maxA, area)
                if st:
                    area = (abs(corner[0]-x) + 1) * (abs(corner[1]-st[-1][1]) + 1)
                    maxA = max(maxA, area)
                else:
                    dirx *= -1
            else:
                corner = st.pop()
                while st and st[-1][0] < x:
                    area = (abs(corner[0]-st[-1][0]) + 1) * (abs(corner[1]-st[-1][1]) + 1)
                    st.pop()
                    maxA = max(maxA, area)

                if st:
                    area = (abs(corner[0]-x) + 1) * (abs(corner[1]-st[-1][1]) + 1)
                    maxA = max(maxA, area)
                else:
                    dirx *= -1
            st.append((x, st[-1][1] if st else y))

        if (diry > 0 and y > st[-1][0]) or (diry < 0  and y < st[-1][0]):
            st.append((y, st[-1][1]))
        else:
            if diry > 0:
                corner = st.pop()
                while st and st[-1][0] > y:
                    area = (abs(corner[0]-st[-1][0]) + 1) * (abs(corner[1]-st[-1][1]) + 1)
                    st.pop()
                    maxA = max(maxA, area)
                if st:
                    area = (abs(corner[0]-st[-1][0]) + 1) * (abs(corner[1]-y) + 1)
                    maxA = max(maxA, area)
                else:
                    diry *= -1
            else:
                corner = st.pop()
                while st and st[-1][0] < y:
                    area = (abs(corner[0]-st[-1][0]) + 1) * (abs(corner[1]-st[-1][1]) + 1)
                    st.pop()
                    maxA = max(maxA, area)
                if st:
                    area = (abs(corner[0]-st[-1][0]) + 1) * (abs(corner[1]-y) + 1)
                    maxA = max(maxA, area)
                else:
                    diry *= -1
            st.append((st[-1][0] if st else x, y))
        print(x, y, maxA)
    print(maxA)
