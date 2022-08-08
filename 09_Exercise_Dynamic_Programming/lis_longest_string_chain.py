# Longest Inceasing ubsequence 

from collections import deque
from unittest import result


words = input().split()

size = [0] * len(words)
parent = [None] * len(words)

best_idx = 0
best_size = 1

for idx in range(len(words)):
    current_word = words[idx]
    current_best_size = 1
    current_parrent = None

    for prev_idx in range(idx - 1, -1, -1):
        prev_word = words[prev_idx]

        if len(prev_word) >= len(current_word):
            continue

        if size[prev_idx] + 1 >= current_best_size:
            current_best_size = size[prev_idx] + 1
            current_parrent = prev_idx

    size[idx] = current_best_size
    parent[idx] = current_parrent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = idx

# print(*size)
# print(*parent)
# print(best_size)

result = deque()

while best_idx is not None:
    result.appendleft(words[best_idx])
    best_idx = parent[best_idx]

print(*result)
