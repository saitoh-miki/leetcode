# %% [897. Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)
# 問題：rightだけのTreeNodeを作成し返せ
# 解法：深さ優先探索をする
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(tn):
            nonlocal head
            if tn:
                dfs(tn.left)
                head.right = head = TreeNode(tn.val)
                dfs(tn.right)

        res = head = TreeNode()
        dfs(root)
        return res.right
