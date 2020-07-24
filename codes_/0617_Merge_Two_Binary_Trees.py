# %% [617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        lft = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        rgt = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0), lft, rgt)
