# %%
from leetcode import *  # noqa

# %% [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        pv, qv = min(p.val, q.val), max(p.val, q.val)
        while not (pv <= root.val <= qv):
            root = root.left if pv <= root.val else root.right
        return root


# %%
tn = to_treenode([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5])
print(show_treenode(tn))
p = tn.left.left
q = tn.left.right.right
print(p.val, q.val)
Solution().lowestCommonAncestor(tn, p, q).val


# %%
