# %% [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return list(calc(root, [root.val])) if root else []

def calc(tn, cur):
    if not tn.left and not tn.right:
        yield '->'.join(map(str, cur))
        return
    if tn.left:
        yield from calc(tn.left, cur + [tn.left.val])
    if tn.right:
        yield from calc(tn.right, cur + [tn.right.val])
