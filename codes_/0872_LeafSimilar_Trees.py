# %% [872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)
# 問題：root1とroot2の葉が同じかどうかを返せ
# 解法：葉を作成する
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return list(leafs(root1)) == list(leafs(root2))


def leafs(tn):
    if tn:
        if not tn.left and not tn.right:
            yield tn.val
        yield from leafs(tn.left)
        yield from leafs(tn.right)
