def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)
    
    # print(*visited, end=' ')


nodes = int(input())
edges = int(input())
graph = {}

for _ in range(edges):
    parent, child = input().split()
    if parent in graph.keys():
        graph[parent].append(child)
    else: 
        graph[parent] = [child]
    if child not in graph.keys():
        graph[child] = []

start = input()
# print(*graph, sep=' ')

visited = set()

dfs(start, graph, visited)

not_visited = set(graph.keys()).difference(visited)
print(*sorted(not_visited))
