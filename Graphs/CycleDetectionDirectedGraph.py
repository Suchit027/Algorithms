class Graph:
    def dfs(self, adjacencyList, visit, rec, curr):
        visit.append(curr)
        rec.append(curr)
        for x in adjacencyList[curr]:
            if x in rec:
                return True
            if x not in visit:
                if self.dfs(adjacencyList, visit, rec, x):
                    return True
        rec.remove(curr)
        return False


if __name__ == '__main__':
    ob = Graph()
    edges = [[1, 0], [3, 0], [0, 2], [2, 3]]
    vertices = 4
    adjacencyList = [[] for x in range(vertices)]
    for x in range(len(edges)):
        adjacencyList[edges[x][0]].append(edges[x][1])
    visit = []
    for x in range(vertices):
        if x not in visit:
            # if valueset is true then cycle exists and we need to break out of the loop
            valueset = ob.dfs(adjacencyList, visit, [], x)
            if valueset:
                print(valueset)
                break
