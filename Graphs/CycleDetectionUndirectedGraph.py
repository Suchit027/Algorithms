class Graph:
    def dfs(self, adjacencyList, visit, rec, curr, par):
        visit.append(curr)
        rec.append(curr)
        for x in adjacencyList[curr]:
            if x is par:
                continue
            if x in rec:
                return True
            if x not in visit:
                if self.dfs(adjacencyList, visit, rec, x, curr):
                    return True
        rec.remove(curr)
        return False


if __name__ == '__main__':
    vertices = 6
    edges = [[0, 1], [0, 4], [4, 5], [1, 2], [2, 3]]
    adjacencyList = [[] for x in range(vertices)]
    for x in range(len(edges)):
        adjacencyList[edges[x][0]].append(edges[x][1])
        adjacencyList[edges[x][1]].append(edges[x][0])
    ob = Graph()
    visit = []
    for x in range(vertices):
        if x not in visit:
            valueset = ob.dfs(adjacencyList, visit, [], x, None)
            if valueset:
                print(valueset)
