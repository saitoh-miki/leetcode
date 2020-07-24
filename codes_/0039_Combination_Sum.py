# %% [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        calc(candidates, target, [], ans)
        return ans


def calc(candidates, target, cur, ans):
    if target <= 0 or not candidates:
        if target == 0:
            ans.append(cur)
        return
    nxt, la = candidates[:-1], candidates[-1]
    for i in range(0, target + 1, la):
        calc(nxt, target - i, [la] * (i // la) + cur, ans)
