def in_bound(row, col, matrix):
    if row < 0:
        return False
    if col < 0:
        return False
    if row >= len(matrix):
        return False
    if col >= len(matrix[0]):
        return False
    return True


def dfs(parent, row, col, matrix, visited):
    if not in_bound(row, col, matrix):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True

    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []
areas = {}
total_areas = 0

for row in range(rows):
    matrix.append(list(input()[:cols]))
    visited.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 0
        areas[key] += 1
        total_areas += 1

print(f"Areas: {total_areas}")
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")
