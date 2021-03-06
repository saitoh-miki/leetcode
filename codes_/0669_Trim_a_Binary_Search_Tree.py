# %% [669. *Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)
# 問題：値がLとRの範囲から外れるものを除け
# 解法：再帰を用いる
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return root
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
