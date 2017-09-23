# coding=utf-8
"""
背景：假设要把长度为 n 厘米的木棒切分为 1 厘米长的小段，但是 1 根木棒只能由 1 人切分，
     当木棒被切分为 3 段后，可以同时由 3 个人分别切分木棒
     求最多有m个人时，最少要切分几次。譬如 n ＝ 8，m ＝ 3 时如下,切分 4 次就可以了。
问题：1.求当 n ＝20，m＝ 3 时的最少切分次数。
     2.求当 n ＝ 100，m＝ 5 时的最少切分次数。
"""


def solution(m: int, n: int, sticks: int) -> int:
    if sticks <= m:
        return 1 + solution(m, n, sticks * 2)
    elif n > sticks > m:
        return 1 + solution(m, n, sticks + m)
    else:
        return 0


def solution_2(m, n, sticks=1):
    count = 0
    while sticks < n:
        sticks += sticks if sticks <= m else m
        count += 1
    return count


if __name__ == '__main__':
    a = solution_2(3, 20, 1)
    b = solution_2(5, 100, 1)
    print(a, b)
