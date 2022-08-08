# Longest common subsequence

cables = [int(x) for x in input().split()]
rows = len(cables)+1
positions = [pos for pos in range(1, rows)]
cols = len(positions)+1

lcs = []
[lcs.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if cables[row-1] == positions[col - 1]:
            lcs[row][col] = lcs[row-1][col-1] + 1
        else:
            lcs[row][col] = max(lcs[row-1][col], lcs[row][col-1])

print(f'Maximum pairs connected: {lcs[rows-1][cols-1]}')
