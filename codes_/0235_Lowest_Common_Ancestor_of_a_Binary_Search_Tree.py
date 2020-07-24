# %% [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        pv, qv = min(p.val, q.val), max(p.val, q.val)
        while not (pv <= root.val <= qv):
            root = root.left if pv <= root.val else root.right
        return root

