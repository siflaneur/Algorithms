# coding=utf-8
"""
问题：斐波那契数列中，可以整除其各位数字之和的前九个数
"""
from functools import lru_cache

from beginner_level.utils import get_all_numbers_sum


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
