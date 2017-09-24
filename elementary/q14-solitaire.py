# coding=utf-8
"""
问题：2014年 FIFA 世界杯决赛圈球队名
     Brazil Croatia Cameroon Chile Greece Uruguay Italy France USA Russia  Spain Australia
     Cote d'Ivoire Costa Rica Switzerland Honduras Bosnia and Herzegovina Iran Germany
     Portugal Belgium Korea Republic Mexico Netherlands Colombia Japan England Ecuador
     Argentina Nigeria Ghana Algeria
     举个例子，如果像下面这样，那么连续 3 个国名之后接龙就结束了（因为没有英文名称以D开头的国家）。
     “Japan” → “Netherlands” → “Switzerland”
     假设每个国名只能使用一次，求能连得最长的顺序，以及相应的国名个数。
     首字母都是大写，而末尾的字母有大写也有小写。
"""

# 标记已使用国家的方法, 递归，深度优先搜索
import pdb

countries = ["Brazil", "Croatia", "Mexico", "Cameroon", "Spain", "Netherlands", "Chile",
             "Australia", "Colombia", "Greece", "Cote d'Ivoire", "Japan", "Uruguay",
             "Costa Rica", "England", "Italy", "Switzerland", "Ecuador", "France",
             "Honduras", "Argentina", "Bosnia and Herzegovina", "Iran", "Nigeria",
             "Germany", "Portugal", "Ghana", "USA", "Belgium", "Algeria", "Russia", "Korea Republic"]

is_used = [False for i in range(len(countries))]

max_depth = 0


def search(prev, depth):
    global max_depth
    is_last = True
    for i, c in enumerate(countries):
        if c[0] == prev[-1].capitalize():
            if not is_used[i]:
                is_last = False
                is_used[i] = True
                search(c, depth=depth + 1)
                is_used[i] = False
    if is_last:
        max_depth = max(max_depth, depth)


for i, c in enumerate(countries):
    is_used[i] = True
    search(c, 1)
    is_used[i] = False

print(max_depth)
