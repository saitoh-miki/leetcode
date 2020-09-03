# %% [717. 1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/)
# 問題：[0], [1, 0], [1, 1]の3種類をいくつか並べてフラットにしたbitsがある。最後が[0]かどうかを返す
# 解法：最後が1ならFalse。最後の0から前方向に1が続く数が偶数ならTrue。
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        return (bits[::-1] + [0]).index(0, 1) % 2 == 1
