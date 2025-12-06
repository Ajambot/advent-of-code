def countAdjacent(grid, i, j):
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if i + x < 0 or i + x >= len(grid):
                continue
            if j + y < 0 or j + y >= len(grid[0]):
                continue
            if grid[i + x][j + y] == '@':
                count += 1
    return count


with open('4.txt') as f:
    grid = []
    for line in f:
        row = []
        for c in line:
            row.append(c)
        grid.append(row)


    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue
            count = countAdjacent(grid, i, j)
            if count < 4:
                res += 1
    print(res)
