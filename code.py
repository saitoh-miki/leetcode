# %%
from leetcode import *  # noqa

# %% [389. *Find the Difference](https://leetcode.com/problems/find-the-difference/)
# 問題：文字列sに1文字追加し、シャッフルした文字列をtとする。追加した文字を返せ
# 解法：collections.Counterを用いる
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((collections.Counter(t) - collections.Counter(s)).keys())[0]


# %%
Solution().twoSum([2, 7, 11, 15], 9)

# %%
from pathlib import Path

p = Path("codes_")
for f in sorted(p.glob("*.py")):
    ss = (s := f.read_text()).splitlines()
    if len(ss) <= 6 and "Counter" in s:
        print(f)


# %%
