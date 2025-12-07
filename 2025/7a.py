with open('7.txt') as f:
    grid:list[list[str]] = []
    for line in f:
        grid.append(list(line.strip()))
    startr, startc = 0, grid[0].index('S')
    q = [(startr, startc)]
    visited = set()
    res = 0
    while q:
        r, c = q.pop()
        if (r, c) in visited:
            continue
        visited.add((r,c))
        if r >= len(grid) - 1:
            continue

        if grid[r][c] in [".", "S"]:
            grid[r][c] = "|"
            q.append((r+1, c))
        else:
            if c+1 < len(grid[0]):
                q.append((r, c+1))
            if c-1 >= 0:
                q.append((r, c-1))
            res += 1
    print(res)
