# %% [104. *Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
# 問題：最大の深さを返せ
# 解法：再帰的に調べる
class Solution:
    def maxDepth(self, root: TreeNode, depth=0) -> int:
        if root is None:
            return depth
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
