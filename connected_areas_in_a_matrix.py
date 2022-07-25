def get_connected_area_size(row, col, rows, cols, matrix, flag):
    if col < 0 \
            or row < 0 \
            or col > cols-1 \
            or row > rows-1 \
            or matrix[row][col] == '*' \
            or (row, col) in flag:
        return 0
    flag.add((row, col))
    result = 1
    result += get_connected_area_size(row - 1, col, rows, cols, matrix, flag)
    result += get_connected_area_size(row, col + 1, rows, cols, matrix, flag)
    result += get_connected_area_size(row + 1, col, rows, cols, matrix, flag)
    result += get_connected_area_size(row, col - 1, rows, cols, matrix, flag)
    return result


rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
    matrix.append(list(input()))

flag = set()
zones = list()
for row in range(rows):
    for col in range(cols):
        size = get_connected_area_size(row, col, rows, cols, matrix, flag)
        if size == 0:
            continue
        zones.append([row, col, size])


print(f'Total areas found: {len(zones)}')
if len(zones):
    sorted_zones = sorted(zones, key=lambda a: -a[2])
    for i, (x, y, n) in enumerate(sorted_zones):
        print(f'Area #{i+1} at ({x}, {y}) size: {n}')

'''
4
9
---*---*-
---*---*-
---*---*-
----*-*--

5
10
*--*---*--
*--*---*--
*--*****--
*--*---*--
*--*---*--

'''
