# %% [563. Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/)
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = [0]
        chk(root, res)
        return res[0]


def chk(tn, res):
    if not tn:
        return 0
    l, r = chk(tn.left, res), chk(tn.right, res)
    res[0] += abs(l - r)
    return tn.val + l + r
