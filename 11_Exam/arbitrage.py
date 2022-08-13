from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight < other.weight

    # def __repr__(self):
    #     return f'{self.first}->{self.second} {self.weight}'

# def prim(node, profit_by_node, graph):
#     tree = {node}
#     pq = PriorityQueue()
#     for edge in graph[node]:
#         pq.put(edge)

#     while not pq.empty():
#         max_edge = pq.get()
#         tree_node, non_tree_node = -1, -1

#         if max_edge.first in tree and max_edge.second not in tree:
#             tree_node, non_tree_node = max_edge.first, max_edge.second
#         elif max_edge.second in tree and max_edge.first not in tree:
#             tree_node, non_tree_node = max_edge.second, max_edge.first
#         if non_tree_node == -1:
#             continue

#         tree.add(non_tree_node)

#         for edge in graph[non_tree_node]:
#             pq.put(edge)

#         # print(tree_node)
#         # print(non_tree_node)
#         # print()
#         # jumps[non_tree_node] = jumps[tree_node] * graph[non_tree_node].weight
#         profit_by_node[non_tree_node] = profit_by_node[tree_node] * max_edge.weight
#         # print(graph[non_tree_node])
#     # print(tree)


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = input().split()
    weight = float(weight)
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start = input()
source = int(input())
destination = int(input())

distance = [float('inf')] * (nodes + 1)
distance[source] = 0

parent = [None] * (nodes +1)

for _ in range(nodes - 1):
    for first, second, weight in graph:
        if distance[first] == float('inf'):
            continue
        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            distance[second] = new_distance
            parent[second] = first


for first, second, weight in graph:
        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            has_negative = True
            print('Undefined')
            break
else:
    path = find_path(parent, destination)
    print(*path)
    print(distance[destination])
