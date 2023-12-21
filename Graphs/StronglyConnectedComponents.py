class Graph:
    def dfs(self, adjacencyList, visit, curr, des):
        if curr == des:
            return True
        visit[curr] = 1
        for x in adjacencyList[curr]:
            if visit[x] == 0:
                if self.dfs(adjacencyList, visit, x, des) is True:
                    return True
        return False

    def isPath(self, src, des, adjacencyList):
        visit = [0] * (len(adjacencyList) + 1)
        return self.dfs(adjacencyList, visit, src, des)

    def findSCC(self, verticeNo, edges):
        ans = []
        is_succ = [0] * (verticeNo + 1)
        adjacencyList = [[] for x in range(verticeNo + 1)]
        for i in range(len(edges)):
            adjacencyList[edges[i][0]].append(edges[i][1])
        for i in range(1, verticeNo + 1):
            if is_succ[i] == 0:
                succ = [i]
                for j in range(i + 1, verticeNo + 1):
                    if is_succ[j] == 0 and self.isPath(i, j, adjacencyList) and self.isPath(j, i, adjacencyList):
                        is_succ[j] = 1
                        succ.append(j)
                ans.append(succ)
        return ans


if __name__ == '__main__':
    ob = Graph()
    vertices = 5
    edges = [[1, 3], [1, 4], [2, 1], [3, 2], [4, 5]]
    ans = ob.findSCC(vertices, edges)
    print('Strongly connected components')
    for x in ans:
        for y in x:
            print(y, end=" ")
        print()
