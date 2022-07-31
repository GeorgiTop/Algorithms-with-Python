def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for chid in graph[node]:
        dfs(chid, destination, graph, visited)


def path_exist(sorce, destination, graph):
    visited = set()
    dfs(sorce, destination, graph, visited)
    return destination in visited


nodes = int(input())
graph = {}
edges = []

for _ in range(nodes):
    node, children_str = input().split(' -> ')
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

result = []
result_total = 0
for sorce, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[sorce] or sorce not in graph[destination]:
        continue
    graph[sorce].remove(destination)
    graph[destination].remove(sorce)

    if path_exist(sorce, destination, graph):
        result.append((sorce, destination))
        result_total += 1
    else:
        graph[sorce].append(destination)
        graph[destination].append(sorce)

print(f'Edges to remove: {result_total}')
for a, b in result:
    print(f'{a} - {b}')