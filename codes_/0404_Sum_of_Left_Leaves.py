# %% [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        r = self.sumOfLeftLeaves(root.right)
        if (p := root.left) and not p.left and not p.right:
            return root.left.val + r
        return self.sumOfLeftLeaves(root.left) + r
