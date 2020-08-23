# %% [98. *Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
class Solution:
    def isValidBST(self, root: TreeNode, lo=-math.inf, up=math.inf) -> bool:
        if root:
            if root.left and not self.isValidBST(root.left, lo, root.val):
                return False
            if root.right and not self.isValidBST(root.right, root.val, up):
                return False
        return lo < root.val < up if root else True
