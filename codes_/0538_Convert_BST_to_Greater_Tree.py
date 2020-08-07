# %% [538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        conv(root, 0)
        return root


def conv(tn, n):
    if not tn:
        return n
    tn.val += conv(tn.right, n)
    return conv(tn.left, tn.val)
