# coding=utf-8
"""
问题：求位于1000~9999，满足类似下述条件的数。
例子：351 → 3×51＝153
     621 → 6×21＝126
     886 → 8×86＝688
     某些数位之间可以没有运算符，但最少要插入 1 个运算符
"""


def solution():
    """
    1000-9999之间，可以直接排除使用 “+" | "-" | ”/“ 的情况
    即仅仅考虑 ”*“ 和 “” 即可
    疑问：Python中 1 * 01不被允许，有没有什么好办法？
    """
    operations = ["*", ""]
    for i in range(1000, 10000):
        for first in operations:
            for second in operations:
                for third in operations:
                    # TODO
                    if '0' in str(i):
                        continue
                    val = "{}{}{}{}{}{}{}".format(str(i)[0], first, str(i)[1], second,
                                                  str(i)[2], third, str(i)[3])
                    if len(val) > 4:
                        if eval(val) == int(str(i)[::-1]):
                            print(i)


if __name__ == '__main__':
    solution()
