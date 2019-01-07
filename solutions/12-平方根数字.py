# coding=utf-8
# Q：求在计算平方根的时候，最早让 0~9 的数字全部出现的最小整数。注意这里只求平方根为正数的情况，
#    并且请分别求包含整数部分的情况和只看小数部分的情况。
#    例如：2的平方根：1.414213562373095048… （0 ~ 9全部出现需要19位）
#  About IEEE 754, Read this page --> http://share.onlinesjtu.com/mod/tab/view.php?id=176


from math import sqrt

# 只看小数部分
def solution_1():
    i = 1
    while True:
        number_set = set()
        # string = "{:.10f}".format(sqrt(i))
        string = f"{sqrt(i):.10f}"
        string = string.split('.')[1]
        for j in string:
            number_set.add(j)
        if len(number_set) == 10:
            return i
        else:
            number_set.clear()
        i += 1


# 整数部分包括一起看
def solution_2():
    start = 1
    while True:
        union = set()
        string = f"{sqrt(start):.10f}"
        string_first = string.split('.')[0]
        string_second = string.split('.')[1][:10 - len(string_first)]
        for s in string_first:
            union.add(s)
        for t in string_second:
            union.add(t)
        if len(union) == 10:
            return start
        else:
            union.clear()
        start += 1


if __name__ == '__main__':
    print(solution_1())
    print(solution_2())
