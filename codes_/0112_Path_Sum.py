# %% [112. Path Sum](https://leetcode.com/problems/path-sum/)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not (r := sum - root.val) and root.left == root.right == None:
            return True
        return self.hasPathSum(root.left, r) or self.hasPathSum(root.right, r)
