# %% [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
# 問題：targetより大きい文字を求めよ。存在しない場合、最初の文字を返せ
# 解法：bisect.bisect_rightを用いる
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect.bisect_right(letters, target) % len(letters)]
