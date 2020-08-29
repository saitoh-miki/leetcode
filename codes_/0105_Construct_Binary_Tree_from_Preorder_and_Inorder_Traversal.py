# %% [105. **Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
# 問題：preorderなリストとinorderなリストからTreeNodeを作成せよ
# 解法：inorderが存在していれば、preorderから先頭を取り出し、その値でinorderを分割し再帰的に構築
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            i = inorder.index(preorder.pop(0))
            res = TreeNode(inorder[i])
            res.left = self.buildTree(preorder, inorder[:i])
            res.right = self.buildTree(preorder, inorder[i + 1 :])
            return res
