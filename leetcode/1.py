graph = [[1, 2], [3], [3], []]


def dfs(graph, path, curr, des, ans):
    if curr == des:
        path.append(curr)
        ans.append(path)
        return ans
    path.append(curr)
    for x in graph[curr]:
        ans = dfs(graph, path, x, des, ans)
        path.remove(x)
    return ans


print(dfs(graph, [], 0, len(graph) - 1, []))
