# %% [108. *Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            i = len(nums) // 2
            return TreeNode(
                nums[i],
                self.sortedArrayToBST(nums[:i]),
                self.sortedArrayToBST(nums[i + 1 :]),
            )
