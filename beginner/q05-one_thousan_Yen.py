# coding=utf-8
"""
问题：求兑换1000日元纸币时会出现多少种组合？注意，不计硬币兑出的先后顺序。
背景：可以用纸币兑换到 10 日元、50 日元、100 日元和 500 日元硬币的组合，
     且每种硬币的数量都足够多。允许机器最多兑换出 15 枚硬币。
"""
import itertools


def solution() -> int:
    """思路：利用标准库的组合迭代出每一种情况，分别计算总和"""
    combination = 0
    coins = [10, 50, 100, 500]
    for count in range(2, 16):
        for i in itertools.combinations_with_replacement(coins, count):
            if sum(i) == 1000:
                combination += 1
    return combination


count = 0


def solution_better(target: int, coins: list, usage: int) -> int:
    """递归版本：用总额减去总额中的最大面额"""
    # TODO
    global count
    coin = coins.pop()
    if not len(coins):
        if target / coin <= usage:
            count += 1
    else:
        for i in range(0, target // coin):
            solution_better(target - coin * i, coins.copy(), usage - 1)


if __name__ == '__main__':
    assert solution() == 20
    solution_better(1000, [10, 50, 100, 500], 15)
    print(count)
    # assert count == 20
