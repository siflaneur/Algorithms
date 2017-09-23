# coding=utf-8
"""
问题：求当所有牌不再变动时，所有背面朝上的牌的数字。
背景：有 100 张写着数字 1~100 的牌，并按顺序排列着。
     最开始所有 牌都是背面朝上放置。某人从第 2 张牌开始，隔 1 张牌翻牌。然后第 2, 4, 6, …, 100 张牌就会变成正面朝上。
     接下来，另一个人从第 3 张牌开始，隔 2 张牌翻牌（原本背面朝上的，翻转成正面朝上；原本正面朝上的，翻转成背面朝上）。
     再接下来， 又有一个人从第 4 张牌开始，隔 3 张牌翻牌。
     像这样，从第 n 张牌开始，每隔 n－1 张牌翻牌，直到没有可翻动的牌为止。
"""


class Card:
    def __init__(self, number: int):
        """
        initialize the card，Set the value all False == 牌背面朝上
        """
        self.__dict__ = dict(zip(range(1, number + 1), [False] * number))

    def flip(self, number: int):
        """
        flip the cards of the N * number
        """
        for key, value in self.__dict__.items():
            if key % number == 0:
                self.__dict__[key] = not value


def solution():
    cards = Card(100)

    for i in range(2, 101):
        cards.flip(i)
    for key, value in cards.__dict__.items():
        if not cards.__dict__[key]:
            print(key)


if __name__ == '__main__':
    solution()
