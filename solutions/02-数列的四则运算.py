# coding = utf-8
# Question: 1000-9999的数字中，对自己各个位的数字做四则运算（加减乘除）最后可以得到自己的回文数的数字有哪些
# 举例，351 -> 3 * 51 = 153 , 621 -> 6 * 21 = 126
# Analysis: 需要嵌套循环，列出表达式后用evel()函数，比较暴力的解法

def solution():
    # 分析：首先我们可以排除掉除法，因为除法需要ABC/D,结果必然不可能为4位数，也可以排除加法和减法，因为同理得不到四位数
    #       所以仅仅考虑怎么把乘号与4个数字组合放置即可。
    operaton = ['*', '']  #  Multiplication,即乘法，但是需要加上空字符
    for i in range(1000, 10000):  # 注意int类型不能遍历，需要转成str
        for first_opera in operaton:
            for second_opera in operaton:
                for third_opera in operaton:
                    if '0' in str(i):
                        continue
                    val = f'{str(i)[0]}{first_opera}{str(i)[1]}{second_opera}{str(i)[2]}{third_opera}{str(i)[3]}'
                    if len(val) > 4:
                        res = eval(val)
                        if str(res) == str(i)[::-1]:
                            return i


print(solution())
