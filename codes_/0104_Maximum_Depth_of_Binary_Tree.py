# %% [104. *Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
class Solution:
    def maxDepth(self, root: TreeNode, depth=0) -> int:
        if root is None:
            return depth
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
