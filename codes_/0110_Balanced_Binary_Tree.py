# %% [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return not math.isinf(check(root))


def check(tn):
    if not tn:
        return 0
    l, r = check(tn.left), check(tn.right)
    return max(l, r) + 1 if abs(l - r) < 2 else math.inf
