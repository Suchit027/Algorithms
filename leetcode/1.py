import heapq
n = 4
k = 2
times = [[2,1,1],[2,3,1],[3,4,1]]
adList = [[] for i in range(n)]
for i in times:
    adList[i[0] - 1].append((i[2], i[1] - 1))
queue = [(0, k - 1)]
dis = [1000000] * n
visit = []
while queue:
    curr = heapq.heappop(queue)
    if curr[1] not in visit:
        visit.append(curr[1])
        for x in adList[curr[1]]:
            if x[0] + dis[curr[1]] < dis[x[1]]:
                dis[x[1]] = dis[curr[1]] + x[0]
                heapq.heappush(queue, (dis[x[1]], x[1]))
if 1000000 in dis:
    print(-1)
print(max(dis))
