# coding = utf-8
# Q:十进制，二进制，八进制下都是回文数字中大于10的最小值


def solution():
    res = 11
    while True:
        # 写出res的二进制和八进制的字符形式
        res_bin = bin(res).lstrip('0b')
        res_oct = oct(res).lstrip('0o')
        if res_bin == res_bin[::-1] and res_oct == res_oct[::-1] and str(res) \
           == str(res)[::-1]:
            return res
        res += 1


print(solution())
