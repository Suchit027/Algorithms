import heapq
from collections import defaultdict


def dijkstra(adList, source):
    visit = []
    distance = defaultdict(lambda: 100000)
    distance[source] = 0
    queue = [(0, source)]
    while queue:
        curr = heapq.heappop(queue)
        if curr[1] not in visit:
            visit.append(curr[1])
            for x in adList[curr[1]]:
                if distance[curr[1]] + x[0] < distance[x[1]]:
                    distance[x[1]] = x[0] + distance[curr[1]]
                    heapq.heappush(queue, (distance[x[1]], x[1]))
    return distance


def minimumCost(source, target, original, changed, cost):
    adList = defaultdict(lambda: [])
    for i in range(len(original)):
        adList[original[i]].append((cost[i], changed[i]))
    src = original[0]

    ans = 0
    distance = dijkstra(adList, src)
    for i in range(len(source)):
        ans += distance[target[i]] - distance[source[i]]

    return ans

if __name__ == '__main__':
    source = "abcd"
    target = "acbe"
    original = ["a","b","c","c","e","d"]
    changed = ["b","c","b","e","b","e"]
    cost = [2,5,5,1,2,20]
    print(minimumCost(source, target, original, changed, cost))
