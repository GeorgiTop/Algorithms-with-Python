def calc_fib(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    result = calc_fib(n-1, memo) + calc_fib(n-2, memo)
    memo[n] = result
    return result


n = int(input())

print(calc_fib(n, {}))