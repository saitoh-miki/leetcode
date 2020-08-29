# %% [83. *Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
# 問題：ソート済みListNodeから要素が重複していれば、その要素すべてを削除せよ
# 解法：whileを2重にし、値が同じ間、要素を削除する
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head
