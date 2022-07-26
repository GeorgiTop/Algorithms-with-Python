def recursive_draw(number):
    if number <= 0:
        return number
    print('*' * number)
    recursive_draw(number-1)
    print('#' * number)


number = int(input())

recursive_draw(number)
