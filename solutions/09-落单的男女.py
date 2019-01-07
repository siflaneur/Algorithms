# coding=utf-8
# 分析: 本题本质是一个最短路径的问题,但是需要去除某些男女人数相同的点


boy, girl = 21, 11

seq = [[0 for _ in range(boy)] for _ in range(girl)]

seq[0][0] = 1
for m in range(girl):
    for n in range(boy):
        if m != n and (boy - n) != (girl - m):
            if n > 0:
                seq[m][n] += seq[m][n - 1]
            if m > 0:
                seq[m][n] += seq[m - 1][n]

print(seq[-2][-1] + seq[-1][-2])
