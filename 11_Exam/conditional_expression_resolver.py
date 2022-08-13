from collections import deque

def is_ternar(a):
    if a == 't':
        return True
    if a == 'f':
        return True
    return False

def left_or_right(a, b, c, list):
    bool = list[a]
    return b if bool == 't' else c

def resolver(idx1, idx2, idx3, list):
    a = list[idx1]
    b = list[idx2]
    c = list[idx3]
    if is_ternar(a) and b.isnumeric() and c.isnumeric():
        return left_or_right(idx1, idx2, idx3, list)
    if is_ternar(b):
        idx3 += 4
        idx2 = left_or_right(idx2, resolver(idx2, idx2+2, idx2+4, list), idx3, list)
    if is_ternar(c):
        idx3 = left_or_right(idx3, idx3+2, resolver(idx3, idx3+2, idx3+4, list), list)
    return left_or_right(idx1, idx2, idx3, list)


line = input().split()

print(line[resolver(0, 2, 4, line)])


# cmds = line[:len(line)//2:2]
# nums = deque(line[len(line)//2::2])

# for _ in range(len(cmds)):
#     a = cmds.pop()
#     b, c = nums.popleft(), nums.popleft()
#     nums.appendleft(left_or_right(a, b, c))

# print(nums[0])


