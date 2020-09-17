# %% [876. *Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
# 問題：ListNodeの中間を返せ（偶数なら後ろ）
# 解法：進み方の異なる2つの変数を用いる
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p = q = head
        while q and q.next:
            p = p.next
            q = q.next.next
        return p
