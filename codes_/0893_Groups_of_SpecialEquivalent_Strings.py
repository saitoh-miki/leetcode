# %% [893. Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/)
# 問題：偶数番目同士または奇数番目同士を交換し一致すれば同一グループ。グループ数を返せ
# 解法：奇数番目を大文字に変えcollections.Counterを用いる
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        cc = [collections.Counter(i[::2].upper() + i[1::2]) for i in A]
        return len(set(tuple(sorted(c.items())) for c in cc))
