# coding=utf-8
"""Code which can be reused"""


def reverse(str_of_number: str):
    """
    #  数字分类别输出，我也不想这么麻烦，但是Python没有内置一个方便的函数
    #  更好的写法是用format(x, 'b'/'o'/'x')去掉0b/0o/0x
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


