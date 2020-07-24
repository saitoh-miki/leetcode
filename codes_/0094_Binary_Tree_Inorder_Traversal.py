# %% [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorderTraversal(root, res := [])
        return res


def inorderTraversal(root, res):
    if root:
        inorderTraversal(root.left, res)
        res.append(root.val)
        inorderTraversal(root.right, res)
