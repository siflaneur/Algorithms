# coding=utf-8


european = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10,
            5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
american = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1,
            00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]


def solution(roulette_type, n):
    ans = 0
    for i in range(len(roulette_type)):
        if i + n <= len(roulette_type):
            tmp = sum(roulette_type[i:i+n])
        else:
            tmp = sum(roulette_type[i:])
            tmp += sum(roulette_type[:(n - (len(roulette_type) - i))])
        ans = max(tmp, ans)
    return ans


if __name__ == '__main__':
    count = 0
    for i in range(2, 37):
        if solution(european, i) < solution(american, i):
            count += 1
    print(count)
