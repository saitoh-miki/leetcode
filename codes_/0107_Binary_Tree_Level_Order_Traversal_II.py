# %% [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans, nxt = [], [root]
        while nxt:
            nxt, cur = [], nxt
            ans.insert(0, lst := [])
            while cur:
                if p := cur.pop(0):
                    lst.append(p.val)
                    nxt.append(p.left)
                    nxt.append(p.right)
        return [i for i in ans if i]
