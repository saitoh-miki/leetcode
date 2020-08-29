# %% [24. *Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
# 問題：2つずつ交換したListNodeを求めよ
# 解法：3つずつ処理
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        top = p = ListNode(0, head)
        while (q := p.next) and (r := q.next):
            p.next, q.next, r.next = r, r.next, q
            p = r.next
        return top.next
