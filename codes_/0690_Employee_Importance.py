# %% [690. Employee Importance](https://leetcode.com/problems/employee-importance/)
# 問題：idに対応するEmployeeとそのsubordinates（idのリスト）の子孫のimportanceの和を求めよ
# 解法：idをキーとする辞書を作成し再帰を用いる
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        dc = {e.id: e for e in employees}
        return calc(dc[id], dc)


def calc(e, dc):
    return e.importance + sum(calc(dc[i], dc) for i in e.subordinates) if e else 0
