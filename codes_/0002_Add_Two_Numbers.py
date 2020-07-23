# %% [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        in1, in2, of, lst = to_iter(l1), to_iter(l2), 0, []
        for n1, n2 in itertools.zip_longest(in1, in2, fillvalue=0):
            val = n1 + n2 + of
            of, val = val // 10, val % 10
            lst.append(val)
        if of:
            lst.append(of)
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
