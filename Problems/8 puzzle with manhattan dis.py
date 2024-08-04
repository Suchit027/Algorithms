class Puzzle:
    def __init__(self, mat, i, j):
        self.mat = mat
        self.blanki = i
        self.blankj = j
        self.heu = 0

    def heuristic(self, goal):
        curr = []
        want = []
        for i in range(3):
            for j in range(3):
                curr.append((self.mat[i][j], i, j))
                want.append((goal[i][j], i, j))
        curr.sort(key=lambda x: x[0])
        want.sort(key=lambda x: x[0])
        for i in range(9):
            self.heu += abs(curr[i][1] - want[i][1]) + abs(curr[i][2] - want[i][2])

    def genlist(self, goal):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        adlist = []
        for i in directions:
            if 0 <= self.blanki + i[0] <= 2 and 0 <= self.blankj + i[1] <= 2:
                mat = [[i for i in self.mat[j]] for j in range(3)]
                mat[self.blanki][self.blankj], mat[self.blanki + i[0]][self.blankj + i[1]] = mat[self.blanki + i[0]][
                    self.blankj + i[1]], mat[self.blanki][self.blankj]
                ob = Puzzle(mat, self.blanki + i[0], self.blankj + i[1])
                ob.heuristic(goal)
                adlist.append(ob)
        return adlist


def astar(src, goal):
    queue = [(src.heu, src, [src.mat])]
    visit, dis = [], {(src.blanki, src.blankj): src.heu}
    while queue:
        curr = queue.pop()
        if curr[1].mat == goal:
            return curr[2]
        if dis[(curr[1].blanki, curr[1].blankj)] != curr[0]:
            continue
        visit.append(curr[1])
        adlist = curr[1].genlist(goal)
        for x in adlist:
            if x.mat not in visit:
                dis[(x.blanki, x.blankj)] = x.heu + curr[0] - curr[1].heu + 1
                path = [i for i in curr[2]]
                path.append(x.mat)
                queue.append((x.heu + curr[0] - curr[1].heu + 1, x, path))
                queue.sort(reverse=True, key=lambda x: x[0])
            else:
                if dis[(x.blanki, x.blankj)] > x.heu + curr[0] - curr[1].heu + 1:
                    dis[(x.blanki, x.blankj)] = x.heu + curr[0] - curr[1].heu + 1
                    path = [i for i in curr[2]]
                    path.append(x.mat)
                    queue.append((x.heu + curr[0] - curr[1].heu + 1, x, path))
                    queue.sort(reverse=True, key=lambda x: x[0])
    return 'no solution'


if __name__ == '__main__':
    s = [[1, 2, 3],
         [5, 6, 0],
         [7, 8, 4]]
    g = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]
    src = Puzzle(s, 1, 2)
    src.heuristic(g)
    x = astar(src, g)
    print(x)
