# coding=utf-8
# Q: 币种有10， 50， 100， 500, 问1000日元有多少种兑换方式（限15枚硬币）
#    不计先后顺序


coins = [10, 50, 100, 500]


def solution():
    res = 0
    for i in range(16):
        for j in range(16):
            for k in range(11):
                for o in range(3):
                    if i+j+k+o <= 15:
                        if 10*i + 50*j + 100*k + 500*o == 1000:
                            res += 1
    return res


if __name__ == "__main__":
    print(solution())  # 20
