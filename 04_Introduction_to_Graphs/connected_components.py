def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)


visited = [False] * len(graph)

for node in range(len(graph)):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    # print('Connected component:', *component)
    print(f"Connected component: {' '.join([str(x) for x in component])}")
