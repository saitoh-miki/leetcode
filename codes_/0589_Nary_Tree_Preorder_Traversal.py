# %% [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
class Solution:
    def preorder(self, root: "Node") -> List[int]:
        return list(dfs(root))


def dfs(nd):
    if nd:
        yield nd.val
        for c in nd.children:
            yield from dfs(c)
