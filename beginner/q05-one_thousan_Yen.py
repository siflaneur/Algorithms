# coding=utf-8
"""
问题：求兑换1000日元纸币时会出现多少种组合？注意，不计硬币兑出的先后顺序。
背景：可以用纸币兑换到 10 日元、50 日元、100 日元和 500 日元硬币的组合，
     且每种硬币的数量都足够多。允许机器最多兑换出 15 枚硬币。
"""
import itertools
from copy import copy


# 暴力版本
def brute_force():
    com = 0
    for coin_500 in range(3):
        for coin_100 in range(11):
            for coin_50 in range(16):
                for coin_10 in range(16):
                    if coin_10 + coin_50 + coin_100 + coin_500 <= 15:
                        if coin_10 * 10 + coin_50 * 50 + coin_100 * 100 + coin_500 * 500 == 1000:
                            com += 1
    return com


def solution():
    """思路：利用标准库的组合迭代出每一种情况，分别计算总和"""
    combination = 0
    coins = [10, 50, 100, 500]
    for cnt in range(2, 16):
        for i in itertools.combinations_with_replacement(coins, cnt):
            if sum(i) == 1000:
                combination += 1
    return combination


count = 0


def solution_better(target, coins, usage):
    """递归版本：用总额减去总额中的最大面额"""
    global count
    coin = coins.pop()
    if not len(coins):
        if target // coin <= usage:
            count += 1
    else:
        for i in range(0, target // coin + 1):
            solution_better(target - coin * i, coins.copy(), usage - i)
