# %% [1038. Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        conv(root, 0)
        return root


def conv(tn, n):
    if not tn:
        return n
    tn.val += conv(tn.right, n)
    return conv(tn.left, tn.val)
