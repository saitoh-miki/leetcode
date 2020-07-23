# %% [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return isSymmetric(root, root)

def isSymmetric(left, right):
    if left and right:
        return (left.val == right.val and
                isSymmetric(left.left, right.right) and
                isSymmetric(left.right, right.left))
    return left is right
