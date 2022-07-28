from webbrowser import get


def get_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return get_fibonacci(n-1)+get_fibonacci(n-2)


fib_n = int(input('Input a number:'))

print(get_fibonacci(fib_n))
