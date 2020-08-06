# %% [783. Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        lst = list(to_list(root))
        return min(abs(i - j) for i, j in zip(lst, lst[1:]))


def to_list(tn, top=False):
    if tn:
        yield from [tn.val] if top else to_list(tn.left, top)
        yield from to_list(tn.left, top) if top else [tn.val]
        yield from to_list(tn.right, top)
