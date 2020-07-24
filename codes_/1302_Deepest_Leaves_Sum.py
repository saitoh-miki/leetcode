# %% [1302. Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        lst = [root]
        while lst:
            pre, lst = lst, [ch for tn in lst if tn for ch in [tn.left, tn.right] if ch]
        return sum(tn.val for tn in pre)
