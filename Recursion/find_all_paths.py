def read_lab():
    rows = int(input())
    cols = int(input())
    return [list(input()[0:cols]) for _ in range(rows)]


def is_inbound(lab, row, col):
    if (0 <= row < len(lab)) and (0 <= col < len(lab[0])):
        return True
    return False


def is_exit(lab, row, col):
    if lab[row][col] == 'e':
        return True
    return False


def is_free(lab, row, col):
    if lab[row][col] == '-':
        return True
    return False


def mark(lab, row, col, tick):
    lab[row][col] = tick


def print_path(path):
    print(''.join(path))


def find_paths(row, col, direction, lab, path):
    if not is_inbound(lab, row, col):
        return

    path.append(direction)

    if is_exit(lab, row, col):
        print_path(path)
    elif is_free(lab, row, col):
        mark(lab, row, col, 'v')
        find_paths(row, col+1, 'R', lab, path)
        find_paths(row, col-1, 'L', lab, path)
        find_paths(row+1, col, 'D', lab, path)
        find_paths(row-1, col, 'U', lab, path)
        mark(lab, row, col, '-')
    
    path.pop()


labirinth = read_lab()
path = []
find_paths(0, 0, '', labirinth, path)
# print(labirinth)
