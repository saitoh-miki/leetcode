# %% [389. *Find the Difference](https://leetcode.com/problems/find-the-difference/)
# 問題：文字列sに1文字追加し、シャッフルした文字列をtとする。追加した文字を返せ
# 解法：collections.Counterを用いる
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((collections.Counter(t) - collections.Counter(s)).keys())[0]
