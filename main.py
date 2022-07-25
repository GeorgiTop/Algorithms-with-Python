def reverse_array(idx, arr):
    if idx == len(elements)//2:
        return 
    last_idx = len(elements) - 1 - idx
    elements[idx], elements[last_idx] = elements[last_idx], elements[idx]
    reverse_array(idx+1, arr)

elements = input("Tell me your stuff:\n").split()

reverse_array(0, elements)
print(" ".join(elements))
