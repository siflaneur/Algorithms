# coding=utf-8


from functools import lru_cache


def get_all_numbers_sum(n):
    tmp = n
    value = 0
    while n > 0:
        value += n % 10
        n //= 10
    return tmp % value == 0


@lru_cache()
def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_validated():
    count = 0
    for i in range(100):
        tmp = fibonacci(i)
        if get_all_numbers_sum(tmp):
            count += 1
            print(tmp)


if __name__ == '__main__':
    is_validated()
