# %% [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        return ((root.val if L <= root.val <= R else 0)
                + (0 if root.val < L else self.rangeSumBST(root.left, L, R))
                + (0 if root.val > R else self.rangeSumBST(root.right, L, R)))
