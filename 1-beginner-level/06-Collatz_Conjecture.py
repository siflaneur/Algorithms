# coding=utf-8
"""
背景：（考拉兹猜想
        ——>>>对自然数 n 循环执行如下操作。
                ·n 是偶数时，用 n 除以 2
                ·n 是奇数时，用 n 乘以3后加1
             如此循环操作的话，无论初始值是什么数字，最终都会得到 1）
     修改一下这个猜想的内容，即假设初始值为偶数时， 也用 n 乘以 3 后加 1，
     但只是在第一次这样操作，后面的循环操作不变。
     而我们要考虑的则是在这个条件下最终又能回到初始值的数。
例子：2 → 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2
     4 → 13 → 40 → 20 → 10 → 5 → 16 →8 → 4
     6 → 19 → 58 → 29 → 88 → 44 → 22 → 11 → 34 → 17 → 52 → 26 → 13 →40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 → 4 → …
问题：求在小于 10000 的偶数中，像上述的 2 或者 4 这样“能回到初始值的数”有多少个。

"""


def is_loop(n):
    check = n
    n = n * 3 + 1
    while n != 1:
        if n == check:
            return True
        elif n % 2 == 0:
            n /= 2
        elif n % 2 == 1:
            n = n * 3 + 1
    return False


def solution(number: int) -> int:
    count = 0
    for i in range(0, number + 1, 2):
        if is_loop(i):
            count += 1
        else:
            continue
    return count


if __name__ == '__main__':
    print(solution(10000))
    assert solution(10000) == 34
