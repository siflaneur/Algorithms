# coding=utf-8
"""
问题：求使下面这个字母算式成立的解法有多少种？
     READ＋ WRITE ＋ TALK ＝ SKILL
"""
from itertools import permutations
import re


# normal solution
def solution(count=0):
    for seq in permutations(range(10), 10):
        [R, E, A, D, W, I, T, L, K, S] = seq
        if R == 0 or W == 0 or T == 0 or S == 0:
            continue
        read = 1000 * R + 100 * E + 10 * A + D
        write = 10000 * W + 1000 * R + 100 * I + 10 * T + E
        talk = 1000 * T + 100 * A + 10 * L + K
        skill = 10000 * S + 1000 * K + 100 * I + 11 * L
        if read + write + talk == skill:
            count += 1
            print('{} + {} + {} = {}'.format(read, write, talk, skill))
    print(count)


# Better version of a more reusable solution
def better_solution(expression):
    # nums = re.split('\W+', expression)
    nums = set()
    for i in re.finditer('\w', expression):
        nums.add(i.group(0))
    # for seq in permutations(range(10), 10):


# TODO


if __name__ == '__main__':
    solution()
    # better_solution('READ＋ WRITE ＋ TALK ＝ SKILL')
