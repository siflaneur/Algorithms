# coding=utf-8
"""
问题：假设分别将 3 根长度相同的绳子摆成 3 个四边形。其中 2 根摆成长方形，剩下 1 根摆成正方形。
     这时，会出现 2 个长方形的面积之和等于正方形面积的情况（假设长方形和正方形的各边长都为整数）。
     例） 绳子长度为20时，可以折出以下这些正方形和长方形。
            第 1 根 长1×宽 9 的长方形 → 面积＝ 9
            第 2 根 长2×宽 8 的长方形 → 面积＝ 16
            第 3 根 长5×宽 5 的正方形 → 面积＝ 25
     进一步改变绳子长度并摆成长方形和正方形，统计满足条件的长方形和正方形的组合。
     这里，将同比整数倍的结果看作同一种解法。
     问：求绳子长度从 1 增长到 500 时，共有多少种组合能使摆出的 2 个长方形面积之和等于正方形的面积？
"""
import pdb
from itertools import combinations, permutations

# 正方形周长是 c ，长方形一的面积为(c-x)(c+x) = c^2 - x^2, 长方形二的面积为 c^2 - (c^2-x^2) = x^2
# 所以面积大小满足勾股定理 c^2 = （c^2 - x^2） + x^2
count = 0

7


def gcd(a, b):
    """通过辗转相除法取最大公因数"""
    if a < b:  # 调换位置，使得a > b，以便a % b取余
        a, b = b, a

    y = a % b
    if y == 0:
        return b
    else:
        a, b = b, y
    return gcd(a, b)


for c in range(1, 126):
    for a, b in combinations(range(1, c), 2):
        if a * a + b * b == c * c and gcd(a, b) == 1:
            print("{} + {} = {}".format(a**2, b**2, c**2))
            count += 1

print(count)
