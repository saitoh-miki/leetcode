class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_listnode(it):
    ln = p = ListNode()
    for i in it:
        p.next = p = ListNode(i)
    return ln.next


def to_iter(ln, isval=True):
    while ln:
        yield ln.val if isval else ln
        ln = ln.next
