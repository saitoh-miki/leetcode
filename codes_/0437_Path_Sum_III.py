# %% [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
class Solution:
    def pathSum(self, root: TreeNode, sum: int, here: bool = False) -> int:
        if not root:
            return 0
        ttl = int(root.val == sum) + self.pathSum(root.left, sum - root.val, True)
        ttl += self.pathSum(root.right, sum - root.val, True)
        if not here:
            ttl += self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return ttl
