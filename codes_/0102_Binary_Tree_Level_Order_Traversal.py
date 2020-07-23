# %% [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, nxt = [], [root]
        while nxt:
            nxt, cur = [], nxt
            ans.append(lst := [])
            while cur:
                if p := cur.pop(0):
                    lst.append(p.val)
                    nxt.append(p.left)
                    nxt.append(p.right)
        return [i for i in ans if i]
