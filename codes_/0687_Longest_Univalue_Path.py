# %% [687. *Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
# 問題：値が同一のパスのホップ数を求めよ
# 解法：関数を作成する。左右を再帰的に実行し最大を更新する。
#       子供が同じ値なら子供の関数値+1。最大は左右の子供の値の和。
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        fn(root, rs := [0])
        return rs[0]


def fn(tn, rs):
    if not tn or not (tn.left or tn.right):
        return 0
    ld = (fn(tl := tn.left, rs) + 1) * bool(tl and tl.val == tn.val)
    rd = (fn(tr := tn.right, rs) + 1) * bool(tr and tr.val == tn.val)
    rs[0] = max(rs[0], ld + rd)
    return max(ld, rd)
