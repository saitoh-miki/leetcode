# %% [345. *Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)
class Solution:
    def reverseVowels(self, s: str) -> str:
        i = reversed([c for c in s if c in "aeiouAEIOU"])
        return "".join(next(i) if c in "aeiouAEIOU" else c for c in s)
