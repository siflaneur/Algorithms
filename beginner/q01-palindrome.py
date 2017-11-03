# coding=utf-8
"""
问题：求用十进制、二进制、八进制表示都是回文数的所有数字中，大于十进制数 10 的最小值。
"""


def is_palidrome(x, flag='d'):
    return format(x, flag)[::-1] == format(x, flag)


def solution():
    number = 11
    while True:
        if is_palidrome(number) and \
                is_palidrome(number, 'b') and \
                is_palidrome(number, 'o'):
            print(number)
            break
        # 二进制数若末尾为0，必然不符合条件
        number += 2


if __name__ == '__main__':
    solution()
