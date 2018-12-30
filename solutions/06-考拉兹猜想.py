# coding=utf-8
# Q：太长不写了


def solution():
    res = 0
    for i in range(0, 10000, 2):
        copy = i
        i = 3 * i + 1
        while i != 1:
            if i == copy:
                res += 1
            if i % 2 == 0:
                i /= 2
            else:
                i = 3 * i + 1
    return res


if __name__ == "__main__":
    print(solution())
