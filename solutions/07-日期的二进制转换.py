# coding=utf-8
# Q:还是太长了，不写了
from datetime import timedelta, date


def solution():
    res = []
    start_date = date(1964, 10, 10)
    end_date = date(2020, 7, 25)
    for i in range(int((end_date - start_date).days) + 1):
        single_date = start_date + timedelta(i)
        time_format = int(single_date.strftime("%Y%m%d"))
        print(time_format)
        if bin(time_format)[2:] == bin(time_format)[::-1][:-2]:
            res.append(time_format)
    return res


if __name__ == "__main__":
    print(solution())
