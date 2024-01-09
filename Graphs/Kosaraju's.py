class Edge:
    def __init__(self, src, des, wt=0):
        self.src = src
        self.des = des
        self.wt = wt


class Graph:
    def topologicalSort(self, adjacencyList, visit, curr, stack):
        if curr in visit:
            return stack
        visit.append(curr)
        for i in range(len(adjacencyList[curr])):
            x = adjacencyList[curr][i]
            stack = self.topologicalSort(adjacencyList, visit, x.des, stack)
        stack.append(curr)
        return stack

    def dfs(self, adjacencyList, curr, visit, scc):
        visit.append(curr)
        scc.append(curr)
        for i in range(len(adjacencyList[curr])):
            x = adjacencyList[curr][i]
            if x.des not in visit:
                scc = self.dfs(adjacencyList, x.des, visit, scc)
        return scc

    def stronglyConnectedComponent(self, adjacencyList, vertices):
        visit = []
        stack = []
        for i in range(vertices):
            if i not in visit:
                stack = self.topologicalSort(adjacencyList, visit, i, stack)
        transposeList = [[] for x in range(vertices)]
        for i in range(len(adjacencyList)):
            for j in range(len(adjacencyList[i])):
                transposeList[adjacencyList[i][j].des].append(Edge(adjacencyList[i][j].des, adjacencyList[i][j].src))
        visit = []
        ans = []
        while stack:
            curr = stack.pop()
            if curr not in visit:
                ans.append(self.dfs(transposeList, curr, visit, []))
        print(ans)


if __name__ == '__main__':
    vertices = 5
    ed1 = Edge(1, 0)
    ed2 = Edge(0, 3)
    ed3 = Edge(2, 1)
    ed4 = Edge(0, 2)
    ed5 = Edge(3, 4)
    adjacencyList = [[ed2, ed4], [ed1], [ed3], [ed5], []]
    ob = Graph()
    ob.stronglyConnectedComponent(adjacencyList, vertices)
