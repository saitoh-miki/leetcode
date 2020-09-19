# %%
from leetcode import *  # noqa

# %% [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


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
