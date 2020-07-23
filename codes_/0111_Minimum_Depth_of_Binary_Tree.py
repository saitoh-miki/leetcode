# %% [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

class Solution:
    def minDepth(self, tn: TreeNode) -> int:
        if not tn:
            return 0
        if None in (tn.left, tn.right):
            return self.minDepth(tn.left or tn.right) + 1
        return min(self.minDepth(tn.left), self.minDepth(tn.right)) + 1
