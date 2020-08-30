# %% [383. *Ransom Note](https://leetcode.com/problems/ransom-note/)
# 問題：ransomNoteの各文字がmagazineに含まれるかを求めよ。magazineの各文字は一度だけ使える
# 解法：collections.Counterを用いる
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (collections.Counter(ransomNote) - collections.Counter(magazine))
