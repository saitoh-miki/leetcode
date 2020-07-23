# %% [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = list(to_iter(head))
        return lst == lst[::-1]

def to_iter(ln):
    while ln:
        yield ln.val
        ln = ln.next
