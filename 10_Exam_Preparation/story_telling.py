from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.appendleft(node)


graph = {}
visited = set()
while True:
    line = input()
    if line == 'End':
        break
    parent, children_str = line.split(' ->')
    children = [child.strip() for child in children_str.split()]
    graph[parent] = children

result = deque()
for node in graph:
    dfs(node, graph, visited, result)

print(*result)
