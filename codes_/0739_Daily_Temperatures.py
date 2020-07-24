# %% [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        desc_poslst = []  # 大きい順の未決定位置
        for i, t in enumerate(T):
            while desc_poslst and T[desc_poslst[-1]] < t:
                ans[desc_poslst.pop()] = i - desc_poslst[-1]
            desc_poslst.append(i)
        return ans
