class Graph:
    def dfs(self, adjacencyList, path, curr, des):
        if curr == des:
            print(path)
            return
        for x in adjacencyList[curr]:
            path.append(x)
            self.dfs(adjacencyList, path, x, des)
            path.remove(x)
        return

    def allPaths(self, vertices, edges, src, target):
        adjacencyList = [[] for x in range(vertices + 1)]
        for i in range(len(edges)):
            adjacencyList[edges[i][0]].append(edges[i][1])
        self.dfs(adjacencyList, [src], src, target)


if __name__ == '__main__':
    ob = Graph()
    v = 6
    edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 4], [3, 5], [4, 5], [5, 6]]
    ob.allPaths(v, edges, 0, 5)
