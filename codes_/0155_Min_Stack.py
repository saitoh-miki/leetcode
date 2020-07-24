# %% [155. Min Stack](https://leetcode.com/problems/min-stack/)
class MinStack(list):
    push = list.append

    def pop(self) -> None:
        super().pop()

    def top(self) -> int:
        return self[-1]

    def getMin(self) -> int:
        return min(self)
