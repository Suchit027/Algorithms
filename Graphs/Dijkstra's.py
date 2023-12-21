import heapq


class Edge:
    def __init__(self, src, des, wt):
        self.u = src
        self.v = des
        self.weight = wt


class Graph:
    def minimumPath(self, adjacencyList, src, vertices):
        distance = [1e7 for x in range(vertices)]
        distance[src] = 0.0
        visit = []
        # priority queue is implemented in python as a list of tuples
        # where the tuple contains the priority as the first element and the value as the next
        # here heap has first index as distance and second as vertice
        heap = [(0.0, src)]
        heapq.heapify(heap)
        # can not use  -  while heap is not []:
        # as it is not like a list anymore. So use it like this
        while heap:
            curr = heapq.heappop(heap)
            if curr[1] not in visit:
                visit.append(curr[1])
                # using range function to avoid checking for edges of last edges
                for i in range(0, len(adjacencyList[curr[1]])):
                    x = adjacencyList[curr[1]][i]
                    # relaxation
                    if distance[x.u] + x.weight < distance[x.v]:
                        distance[x.v] = distance[x.u] + x.weight
                        heapq.heappush(heap, (distance[x.v], x.v))
        print(distance)


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
    ob.minimumPath(adjacencyList, 0, vertices)
