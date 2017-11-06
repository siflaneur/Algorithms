# coding=utf-8
"""
问题：假设有一款不会反复清扫同一个地方的机器人，它只能前后左右移动。
    举个例子，如果第 1 次向后移动，那么连续移动 3 次时，就会有以 下 9 种情况（图6）。
    又因为第 1 次移动可以是前后左右 4 种情况，所以移动 3 次时全部路径有 9×4 ＝ 36 种。
"""


def solution(searched, n):
    """
    利用深度优先搜索的原理，递归版本
    :param searched: A list like [[0, 0], ...]
    :param n: 即机器人行走的步数
    :return count: all possibilities
    """
    count = 0
    if len(searched) == n + 1:
        return 1
    for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_position = [searched[-1][0] + d[0], searched[-1][1] + d[1]]
        if next_position not in searched:
            count += solution(searched + [next_position], n)
    return count
