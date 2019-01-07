# coding=utf-8
# Q: tldw = (too long, don't write)
# A: 利用深度优先搜索，将扫地机器人起点定为（0， 0）， 将经过的点储存到一个list中来
#    避开已经走过的点


def solution(searched, n):
    count = 0
    if len(searched) == n + 1:
        return 1
    for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_position = [searched[-1][0] + d[0], searched[-1][1] + d[1]]
        if next_position not in searched:
            count += solution(searched + [next_position], n)
    return count


if __name__ == '__main__':
    print(solution([[0, 0]], 12))
