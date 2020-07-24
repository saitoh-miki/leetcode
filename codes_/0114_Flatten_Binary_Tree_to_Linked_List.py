# %% [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lst = list(to_list(p := root, True))
        if root:
            root.left = None
        for i in lst[1:]:
            p.right = p = TreeNode(i)


def to_list(tn, top=False):
    if tn:
        yield from [tn.val] if top else to_list(tn.left, top)
        yield from to_list(tn.left, top) if top else [tn.val]
        yield from to_list(tn.right, top)
