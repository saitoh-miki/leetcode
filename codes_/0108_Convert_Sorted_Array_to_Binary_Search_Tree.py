# %% [108. *Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
# 問題：ソート済みリストから深さが平衡したTreeNodeを作成せよ
# 解法：中央値を元に再帰的に作成
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            i = len(nums) // 2
            return TreeNode(
                nums[i],
                self.sortedArrayToBST(nums[:i]),
                self.sortedArrayToBST(nums[i + 1 :]),
            )
