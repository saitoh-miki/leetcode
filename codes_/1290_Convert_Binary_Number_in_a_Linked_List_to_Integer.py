# %% [1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return int(''.join(str(i) for i in to_iter(head)), 2)

def to_iter(ln, isval=True):
    while ln:
        yield ln.val if isval else ln
        ln = ln.next
