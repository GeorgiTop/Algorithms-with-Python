def generate_vector(idx, arr):
    if idx == len(arr):
        print(*arr, sep='')
        return
    for n in range(0, 2):
        vector[idx] = n
        generate_vector(idx+1, arr)

number = int(input())
vector = [ None for _ in range(number)]

generate_vector(0, vector)