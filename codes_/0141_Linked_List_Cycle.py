# %% [141. *Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
# 問題：ListNodeがサイクルかどうかを返す
# 解法：1つずつ進むポインタと2つずつ進むポインタを使う
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        q = p.next if p else p
        while q and q != p:
            p = p.next
            q = q.next
            q = q.next if q else q
        return q
