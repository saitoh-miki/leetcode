# %% [821. Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)
# 問題：Sの各文字がCからどれくらい離れているかをリストで返せ
# 解法：前方からと後方からの2回走査する
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res, n = [], len(S)
        last = -n
        for i, c in enumerate(S):
            if c == C:
                last = i
            res.append(i - last)
        last = -n
        for i, c in enumerate(S[::-1]):
            if c == C:
                last = i
            res[n - i - 1] = min(res[n - i - 1], i - last)
        return res
