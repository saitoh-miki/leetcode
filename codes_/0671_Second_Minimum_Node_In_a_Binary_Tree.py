# %% [671. Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/)
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        lst = sorted(set(to_list(root)))
        return lst[1] if len(lst) > 1 else -1


def to_list(tn, top=False):
    if tn:
        yield from [tn.val] if top else to_list(tn.left, top)
        yield from to_list(tn.left, top) if top else [tn.val]
        yield from to_list(tn.right, top)
