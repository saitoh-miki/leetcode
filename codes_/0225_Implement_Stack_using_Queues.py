# %% [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
class MyStack(list):
    push = list.append

    def top(self) -> int:
        return self[-1]

    def empty(self) -> bool:
        return not len(self)
