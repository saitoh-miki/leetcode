# %% [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        return self.getTargetCopy(
            original.left, cloned.left, target
        ) or self.getTargetCopy(original.right, cloned.right, target)
