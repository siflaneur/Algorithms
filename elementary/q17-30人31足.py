# coding=utf-8
"""
问题： 30人排队，男女人数不限，任意两个女生不排在一起一共有几种
"""
import pdb

#  递归版本
boy, girl = 'B', 'G'


def insert(seq):
    if len(seq) == 4:
        return 1
    count = insert(seq + boy)
    if seq[-1] == 'B':
        count += insert(seq + girl)
    return count


#  斐波那契版本
#  解释参考-->https://twitter.com/flaneur_dummy/status/912335023633686528
def solution():
    boy, girl = 1, 0
    for i in range(30):
        boy, girl = boy + girl, boy
    print(boy + girl)


if __name__ == '__main__':
    print(insert(boy) + insert(girl))
    solution()
