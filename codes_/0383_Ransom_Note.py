# %% [383. *Ransom Note](https://leetcode.com/problems/ransom-note/)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (collections.Counter(ransomNote) - collections.Counter(magazine))
