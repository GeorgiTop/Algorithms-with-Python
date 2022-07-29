from webbrowser import get


def get_fibonacci(n):
    if n <= 1:
        return 1
    return get_fibonacci(n-1)+get_fibonacci(n-2)


fib_n = int(input())

print(get_fibonacci(fib_n))
