# %% [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        lst = list(to_iter(head))
        n = len(lst)
        for i in range(0, n, k):
            if i + k <= n:
                lst[i : i + k] = reversed(lst[i : i + k])
        return to_listnode(lst)


def to_listnode(it):
    ln = p = ListNode()
    for i in it:
        p.next = p = ListNode(i)
    return ln.next


def to_iter(ln, isval=True):
    while ln:
        yield ln.val if isval else ln
        ln = ln.next
