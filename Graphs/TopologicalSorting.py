class Graph:
    def dfs(self, adjacencyList, visit, stack, curr):
        if visit[curr] == 1:
            return stack
        visit[curr] = 1
        for x in adjacencyList[curr]:
            stack = self.dfs(adjacencyList, visit, stack, x)
        stack.append(curr)
        return stack


if __name__ == '__main__':
    edges = [[5, 0], [5, 2], [2, 3], [3, 1], [4, 1], [4, 0]]
    vertices = 6
    adjacencyList = [[] for x in range(vertices)]
    for x in range(len(edges)):
        adjacencyList[edges[x][0]].append(edges[x][1])
    visit = [0] * (vertices)
    stack = []
    ob = Graph()
    for x in range(vertices):
        if visit[x] == 0:
            stack = ob.dfs(adjacencyList, visit, stack, x)
    stack.reverse()
    print(stack)
