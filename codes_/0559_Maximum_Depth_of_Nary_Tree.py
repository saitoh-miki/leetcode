# %% [559. *Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)
# 問題：最大深さを求めよ
# 解法：幅優先探索せよ
class Solution:
    def *maxDepth(self, root: "Node") -> int:
        if not root or not root.children:
            return int(bool(root))
        return max(self.maxDepth(c) for c in root.children) + 1
