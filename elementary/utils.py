# coding=utf-8

def get_all_numbers_sum(n):
    tmp = n
    value = 0
    while n > 0:
        value += n % 10
        n //= 10
    return tmp % value == 0
