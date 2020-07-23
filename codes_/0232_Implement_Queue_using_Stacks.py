# %% [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

class MyQueue(collections.deque):
    push = collections.deque.appendleft
    def peek(self) -> int:
        return self[-1]
    def empty(self) -> bool:
        return not len(self)
