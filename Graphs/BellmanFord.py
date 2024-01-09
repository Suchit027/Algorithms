# important
# this does not work for negative weighted graphs
# this is because the negative cycle will lead to an endless loop
class Edge:
    def __init__(self, src, des, wt):
        self.u = src
        self.v = des
        self.weight = wt


class Graph:
    def minimumPath(self, adjacencyList, vertices, src):
        distance = [1e7 for x in range(vertices)]
        distance[src] = 0.0
        for i in range(vertices - 1):
            for x in adjacencyList:
                for y in x:
                    if distance[y.u] + y.weight < distance[y.v] and distance[y.u] != 1e7:
                        distance[y.v] = y.weight + distance[y.u]
        print(distance)
        # detecting negative cycles
        for i in range(vertices - 1):
            for x in adjacencyList:
                for y in x:
                    if distance[y.u] + y.weight < distance[y.v] and distance[y.u] != 1e7:
                        print(f'negative cycle present')


if __name__ == '__main__':
    vertices = 6
    ed1 = Edge(0, 1, 2)
    ed2 = Edge(0, 2, 4)
    ed3 = Edge(1, 3, 7)
    ed4 = Edge(1, 2, 1)
    ed5 = Edge(2, 4, 3)
    ed6 = Edge(4, 3, 2)
    ed7 = Edge(3, 5, 1)
    ed8 = Edge(4, 5, 5)
    adjacencyList = [[ed1, ed2], [ed3, ed4], [ed5], [ed7], [ed8, ed6], []]
    ob = Graph()
    ob.minimumPath(adjacencyList, vertices, 0)
