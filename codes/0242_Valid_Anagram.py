# %% [242. *Valid Anagram](https://leetcode.com/problems/valid-anagram/)
# 問題：2つの文字列がアナグラムかどうかを返す
# 解法：collections.Counterを用いる
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
