# %% [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        st = {id(ln) for ln in to_iter(headA, False)}
        for ln in to_iter(headB, False):
            if id(ln) in st:
                return ln


def to_iter(ln, isval=True):
    while ln:
        yield ln.val if isval else ln
        ln = ln.next
