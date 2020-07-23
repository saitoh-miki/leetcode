# %% [1315. Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/)

class Solution:
    def sumEvenGrandparent(self, root: TreeNode, grp=1, par=1) -> int:
        if not root:
            return 0
        return ((0 if grp % 2 else root.val)
                + self.sumEvenGrandparent(root.left, par, root.val)
                + self.sumEvenGrandparent(root.right, par, root.val))
