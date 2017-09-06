# coding=utf-8
"""
问题：求用十进制、二进制、八进制表示都是回文数的所有数字中，大于十进制数 10 的最小值。
"""


def reverse(str_of_number: str):
    """
    slice operation fullfill the reverse operation
    :param str_of_number: str
    :return: str
    """
    if str_of_number.startswith('0b'):
        str_of_number = str_of_number[2:]
        return '0b' + str_of_number[::-1]
    if str_of_number.startswith('0o'):
        str_of_number = str_of_number[2:]
        return '0o' + str_of_number[::-1]
    else:
        return str_of_number[::-1]


def solution():
    number = 11
    while True:
        if reverse(str(number)) == str(number) and \
                        reverse(oct(number)) == oct(number) and \
                        reverse(bin(number)) == bin(number):
            print(number)
            break
        number += 2  # 二进制数若末尾为0，必然不符合条件


if __name__ == '__main__':
    solution()
