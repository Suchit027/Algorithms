import heapq


class Edge:
    def __init__(self, src, des, wt):
        self.src = src
        self.des = des
        self.wt = wt


class Graph:
    def minimumSpanningTree(self, adjacencyList, vertices, src):
        visit = []
        heap = [(0.0, src)]
        heapq.heapify(heap)
        cost = 0
        while heap:
            curr = heapq.heappop(heap)
            if curr[1] not in visit:
                cost += curr[0]
                visit.append(curr[1])
                for i in range(len(adjacencyList[curr[1]])):
                    x = adjacencyList[curr[1]][i]
                    if x.des not in visit:
                        heapq.heappush(heap, (x.wt, x.des))
        print(f'cost = {cost}')

if __name__ == '__main__':
    vertices = 4
    ed1 = Edge(0, 1, 10)
    ed2 = Edge(0, 2, 15)
    ed3 = Edge(0, 3, 30)
    ed4 = Edge(1, 3, 40)
    ed5 = Edge(2, 3, 50)
    ed6 = Edge(1, 0, 10)
    ed7 = Edge(2, 0, 15)
    ed8 = Edge(3, 0, 30)
    ed9 = Edge(3, 1, 40)
    ed10 = Edge(3, 2, 50)
    adjacencyList = [[ed1, ed2, ed3], [ed4, ed6], [ed5, ed7], [ed8, ed9, ed10]]
    ob = Graph()
    ob.minimumSpanningTree(adjacencyList, vertices, 0)