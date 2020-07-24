# %% [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, nxt = [], [root]
        while nxt:
            nxt, cur, lst = [], nxt, []
            while cur:
                if p := cur.pop(0):
                    lst.append(p.val)
                    nxt.append(p.left)
                    nxt.append(p.right)
            if len(ans) % 2:
                lst.reverse()
            ans.append(lst)
        return [i for i in ans if i]
