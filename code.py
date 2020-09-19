# %%
from leetcode import *  # noqa
from leetcode import List

# %% [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


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
