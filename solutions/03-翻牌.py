# coding = utf-8
# Question: 太长，不打了

def solution(n):
    Array = [False] * n  # 模拟背面向上的100张卡牌
    for i in range(2, n + 1):
        j = i - 1
        while j < n:
            Array[j] = not Array[j]
            j += i
    for index, value in enumerate(Array):
        if value == False:
            print(index + 1)


if __name__ == "__main__":
    solution(100)
    