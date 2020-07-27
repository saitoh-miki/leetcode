# %% [482. License Key Formatting](https://leetcode.com/problems/license-key-formatting/)
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace("-", "")[::-1]
        return "-".join(S[i : i + K] for i in range(0, len(S), K))[::-1]
