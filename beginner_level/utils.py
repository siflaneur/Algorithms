# coding=utf-8
"""Code which can be reused"""


def reverse(str_of_number: str):
    """
    数字分类别输出，我也不想这么麻烦，但是Python没有内置一个方便的函数
    :param str_of_number: str
    :return: str
    """
    if str_of_number.startswith('0b'):
        str_of_number = str_of_number[2:]
        return '0b' + str_of_number[::-1]
    elif str_of_number.startswith('0o'):
        str_of_number = str_of_number[2:]
        return '0o' + str_of_number[::-1]
    elif str_of_number.startswith('0x'):
        str_of_number = str_of_number[2:]
        return '0o' + str_of_number[::-1]
    else:
        return str_of_number[::-1]


def get_all_numbers_sum(n):
    tmp = n
    value = 0
    while n > 0:
        value += n % 10
        n //= 10
    return tmp % value == 0
