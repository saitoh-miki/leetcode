# %%
from leetcode import *  # noqa

# %% [46. Permutations](https://leetcode.com/problems/permutations/)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


# %%
Solution().twoSum([2, 7, 11, 15], 9)

# %%
from pathlib import Path

p = Path("codes_")
for f in sorted(p.glob("*.py")):
    ss = f.read_text().splitlines()
    if len(ss) <= 5:
        print(f)
# %%
