# %%
from leetcode import *  # noqa

# %% [231. Power of Two](https://leetcode.com/problems/power-of-two/)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count("1") == 1


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
