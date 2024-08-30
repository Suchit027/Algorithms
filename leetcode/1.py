def countSubIslands(grid1, grid2):
    direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ans = 0
    visit = set()
    m, n = len(grid1), len(grid1[0])
    def helper(i, j):
        visit.add((i, j))
        ret = True
        for x, y in direc:
            a = i + x
            b = j + y
            if 0 <= a < m and 0 <= b < n and grid2[a][b] == 1 and (a, b) not in visit:
                if grid1[a][b] == 0:
                    helper(a, b)
                    ret = False
                else:
                    ret = ret & helper(a, b)
        return ret

    for i in range(m):
        for j in range(n):
            if (i, j) in visit:
                continue
            if grid2[i][j] == 1 and grid1[i][j] == 1:
                if helper(i, j):
                    print(f'{i} {j}')
                    ans += 1
    print(sorted(visit))
    return ans


print(countSubIslands(
    [[1, 1, 1, 1, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0],
     [1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0]],
    [[1, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0],
     [0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0]]))
