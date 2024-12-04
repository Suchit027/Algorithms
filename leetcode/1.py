def smallestRange(nums):
    store = []
    n = len(nums)
    for i in range(n):
        for x in nums[i]:
            store.append([x, i])

    store.sort()

    ans = [float('-inf'), float('inf')]
    l = len(store)

    for i in range(l):
        visit, j = set(i for i in range(n)), i
        while j < l and len(visit) > 0:
            visit.discard(store[j][1])
            j += 1
        if j < l:
            ans = min(ans, [store[i][0], store[j][0]], key=lambda x: x[1] - x[0])

    return ans

print(smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))