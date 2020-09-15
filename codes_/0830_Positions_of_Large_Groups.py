# %% [830. Positions of Large Groups](https://leetcode.com/problems/positions-of-large-groups/)
# 問題：サイズが3以上の（同じ文字が連続する）グループの「開始位置と終了位置」をリストで返せ
# 解法：文字の変わる位置を保持する
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res, st, pr = [], 0, ""
        for i, c in enumerate(s + ";"):
            if c != pr:
                if i - st >= 3:
                    res.append([st, i - 1])
                st, pr = i, c
        return res
