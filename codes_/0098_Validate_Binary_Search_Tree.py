# %% [98. *Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
# 問題：TreeNodeがinorderで小さい順かどうかを返せ
# 解法：TreeNodeが範囲に入っているかどうか再帰的に調べる
class Solution:
    def isValidBST(self, root: TreeNode, lo=-math.inf, up=math.inf) -> bool:
        if root:
            if root.left and not self.isValidBST(root.left, lo, root.val):
                return False
            if root.right and not self.isValidBST(root.right, root.val, up):
                return False
        return lo < root.val < up if root else True
