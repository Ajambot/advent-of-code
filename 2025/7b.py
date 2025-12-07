memo = {}

def dfs(grid, r, c):
    if c < 0 or c >= len(grid[0])+1:
        return 0
    if (r, c) in memo:
        return memo[(r, c)]
    if r == len(grid)-1:
        memo[(r,c)] = 1
        return memo[(r,c)]
    if grid[r][c] in ['.', 'S']:
        memo[(r,c)] = dfs(grid, r+1, c)
        return memo[(r,c)]
    else:
        memo[(r,c)] = dfs(grid, r, c-1) + dfs(grid, r, c+1)
        return memo[(r,c)]

with open('7.txt') as f:
    grid:list[list[str]] = []
    for line in f:
        grid.append(list(line.strip()))
    startr, startc = 0, grid[0].index('S')
    print(dfs(grid, startr, startc))
