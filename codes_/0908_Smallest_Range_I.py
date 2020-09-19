# %% [908. *Smallest Range I](https://leetcode.com/problems/smallest-range-i/)
# 問題：条件（abs(b-a)<=K）を満たす最小のBの範囲（最大−最小）を返せ
# 解法：K==0ならmax(A)-min(A)。範囲は2*Kだけ狭められる
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2 * K)
