# coding=utf-8
"""
#背景：A上楼梯时，B 从同一楼梯往下走。每次不一定只走 1 级，最多可 以一次跳过 3 级（即直接前进 4 级）。 但无论走多少级，1 次移动所需时间不变。两人同时开始走，求共 B
有多少种“两人最终同时停在同一级” 的情况（假设楼梯宽度足够，可以相互 错开，不会撞上。另外，同时到达同一
级时视为结束）。
#问题：求当存在 10 级楼梯，且移动规则相同时，有多少种两人最终同时停在同一 级的情况？
"""
from functools import lru_cache


def memo(func):
    """
    # remember that list cannot be hashed, use set or tuple
    """
    memory = dict()

    def wrap(a, b):
        if (a, b) not in memory:
            memory[(a, b)] = func(a, b)
        return memory[(a, b)]

    return wrap


@memo
def move(a, b):
    """
    #1. Normal_solution:use two loops manipulating the walking step
    #2. Memorization_solution:
    :param a: int
    :param b: int
    :return: count -> int
    """
    count = 0
    if a > b:
        return 0
    if a == b:
        return 1
    for i in range(1, 4):
        for j in range(1, 4):
            count += move(a + i, b - j)
    return count


if __name__ == '__main__':
    print(move(0, 10))
