def islandPerimeter(grid):
    store = {1: 0, 2: 0, 3: 0}
    m, n = len(grid), len(grid[0])
    visit = set()
    direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(i, j):
        visit.add((i, j))
        surr = 0
        if i > 0:
            surr = grid[i - 1][j]
        if i < m - 1:
            surr += grid[i + 1][j]
        if j > 0:
            surr += grid[i][j - 1]
        if j < n - 1:
            surr += grid[i][j + 1]
        if surr < 4:
            store[surr] += 1
        for x, y in direc:
            a = i + x
            b = j + y
            if 0 <= a < m and 0 <= b < n and (a, b) not in visit and grid[a][b] == 1:
                dfs(a, b)
        return

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                break
    ans = (store[1] * 3) + (store[2] * 2) + (store[3])
    return ans

print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))