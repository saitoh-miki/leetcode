# %% [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return dfs(root, 0)[1]

def dfs(tn, mx):
    if not tn:
        return 0, mx
    nl, mx = dfs(tn.left, mx)
    nr, mx = dfs(tn.right, mx)
    return max(nl, nr) + 1, max(mx, nl + nr)
