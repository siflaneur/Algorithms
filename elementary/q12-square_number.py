# coding=utf-8
"""
问题：求在计算平方根的时候，最早让 0~9 的数字全部出现的最小整数。注意这里只求平方根为正数的情况，
     并且请分别求包含整数部分的情况和只看小数部分的情况。
     例如：2的平方根：1.414213562373095048… （0 ~ 9全部出现需要19位）
"""
#  About IEEE 754, Read this page --> http://share.onlinesjtu.com/mod/tab/view.php?id=176
from math import sqrt

i = 1
while True:
    number_set = set()
    string = "{:.10f}".format(sqrt(i))
    string = string.split('.')[1]
    for j in string:
        number_set.add(j)
    if len(number_set) == 10:  # 算上符号"."
        print(i)
        break
    else:
        number_set.clear()
    i += 1


assert i == 143
