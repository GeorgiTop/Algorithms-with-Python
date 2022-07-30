def calc_array_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + calc_array_sum(numbers, idx + 1)

numbers = list(map(int, input().strip().split(' ')))

print(calc_array_sum(numbers, 0))
