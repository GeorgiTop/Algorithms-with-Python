class Area():
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


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
        zones.append(Area(row, col, size))


print(f'Total areas found: {len(zones)}')
for i, area in enumerate(sorted(zones, key=lambda area: area.size, reverse=True)):
    print(f'Area #{i+1} at ({area.row}, {area.col}) size: {area.size}')

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

2
2
**
**

'''
