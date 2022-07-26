from ast import For


def nest_loop(idx, arr):
    if idx == len(arr):
        print(*arr)
        return
    for n in range(1, len(arr) + 1):
        arr[idx] = n
        nest_loop(idx+1, arr)


nest_size = int(input())
nest = [None] * nest_size
nest_loop(0, nest)
