"""
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值都大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋
盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

比如：
1  10 3  8
12 2  9  6
5  7  4  11
3  7  16 5

最大的路线为(1,12,5,7,7,16,5),那么我们能拿到最大价值为53的礼物
"""


class GiftMaxValue:
    def get_max_value(self, matrix):
        pass