# %% [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
# 問題：costの先頭から1歩または2歩ずつ進み最後までたどる。たどった値の和の最小を返せ
# 解法：1段目と2段目の最小をfirst, secondとし、1つずつずらして更新する
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second, pos, n = cost[0], cost[1], 2, len(cost)
        while pos < n:
            first, second, pos = second, cost[pos] + min(first, second), pos + 1
        return min(first, second)
