# %% [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
# 問題：根がvalに一致するTreeNodeを返せ
# 解法：再帰を用いる
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)
