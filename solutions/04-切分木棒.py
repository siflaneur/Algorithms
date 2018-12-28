# coding = utf-8
# Question: 切分一根N厘米木棒只能一个人，但是两根N/2厘米的木棒可以两个人同时切，
#           直到最后只剩1cm，问20cm木棒3个人最少切多少次/ 100cm木棒5个人呢？


def solution(n, m):  # n代表木棒长度，m为人数
    count = 0
#  采用逆向逻辑，1cm木棒黏合来做, 需要注意的就是人数决定了可以一次粘合多少根木棒
    stick = 1
    while n > stick:
        if stick < m:
            stick += stick
        else:
            stick += m
        count += 1
    return count


if __name__ == "__main__":
    print(solution(20, 3))
    print(solution(100, 5))
