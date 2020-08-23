# %% [606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        sl = f"({self.tree2str(t.left)})" if t.left else "()" if t.right else ""
        sr = f"({self.tree2str(t.right)})" if t.right else ""
        return f"{t.val}{sl}{sr}"
