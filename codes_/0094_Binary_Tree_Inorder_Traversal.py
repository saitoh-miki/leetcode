# %% [94. *Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
# 問題：inorderで出力せよ
# 解法：「左の子処理、値出力、右の子処理」を再帰する
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorderTraversal(root, res := [])
        return res


def inorderTraversal(root, res):
    if root:
        inorderTraversal(root.left, res)
        res.append(root.val)
        inorderTraversal(root.right, res)
