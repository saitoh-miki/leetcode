# %% [3. *Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
# 問題：「すべて異なる文字列」となる部分文字列の最大長を返す
# 解法：今見ている文字が最後に現れたインデックス＋1から今の位置までで更新
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, i, n, idx = 0, 0, len(s), {}
        for j, c in enumerate(s):
            i = max(i, idx.get(c, 0))
            res = max(res, j - i + 1)
            idx[c] = j + 1
        return res
