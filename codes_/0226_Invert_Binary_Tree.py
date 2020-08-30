# %% [226. *Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
# 問題：TreeNodeを左右反転せよ
# 解法：子要素を変換し、子要素をswapする
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root
