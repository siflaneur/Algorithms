# coding=utf-8
"""
问题：把年月日表示为 YYYYMMDD 这样的 8 位整数，然后把这个整数转换成二进制数并且逆序排列，
    再把得到的二进制数转换成十进制数，求与原日期一致的日期。
    求得的日期要在上一次东京奥运会（1964 年 10 月 10 日）到下一次东京奥运会（预定举办日期为 2020 年 7 月 24 日）之间。
"""
from datetime import timedelta, date

from utils import reverse

start_date = date(1964, 10, 10)
end_date = date(2020, 7, 25)


def date_generator(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        single_date = start_date + timedelta(n)
        yield int(single_date.strftime("%Y%m%d"))


def solution():
    for each_date in date_generator(start_date, end_date):
        if reverse(bin(each_date)) == bin(each_date):
            print(each_date)


if __name__ == '__main__':
    solution()
