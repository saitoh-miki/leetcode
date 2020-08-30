# %% [687. *Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
# 問題：「パス中の要素が同一の値のパス」の最大エッジ数を求めよ
# 解法：対象の関数では、左右を再帰的に実行し最大を更新する。
#       子供の値＝「子供が親と同じ値なら、子供の関数値+1。そうでないなら０」
#       最大は、左右の子供の値の和で更新。
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
