# %% [27. *Remove Element](https://leetcode.com/problems/remove-element/)
# 問題：numsからvalに等しい要素を削除し長さを返せ
# 解法：先頭から対象要素で埋めていく（see 26）
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for v in nums:
            if v != val:
                nums[i] = v
                i += 1
        return i
