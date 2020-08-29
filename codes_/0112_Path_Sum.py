# %% [112. *Path Sum](https://leetcode.com/problems/path-sum/)
# 問題：sumに等しいパス（根から葉まで）が存在するかどうかを返す
# 解法：Noneか両子要素がないかそれ以外で場合分けせよ
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not (r := sum - root.val) and root.left == root.right == None:
            return True
        return self.hasPathSum(root.left, r) or self.hasPathSum(root.right, r)
