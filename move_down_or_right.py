def get_paths(c, r, rows, cols):
    if c == cols-1 and r == rows-1:
        return 1
    if c > cols-1 or r > rows-1:
        return 0
    count = 0
    count += get_paths(c+1, r, rows, cols)
    count += get_paths(c, r+1, rows, cols)
    return count


rows = int(input())
cols = int(input())

print(get_paths(0, 0, rows, cols))
