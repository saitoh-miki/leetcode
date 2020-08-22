# %% [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        return list(dfs(root))


def dfs(nd):
    if nd:
        for c in nd.children:
            yield from dfs(c)
        yield nd.val
