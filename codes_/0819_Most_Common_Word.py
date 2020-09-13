# %% [819. Most Common Word](https://leetcode.com/problems/most-common-word/)
# 問題：bannedに含まれない最頻単語を返せ（大文字は小文字とみなす）
# 解法：collections.Counterを用いる
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c = collections.Counter(re.findall(r"\w+", paragraph.lower()))
        return next(s for s, _ in c.most_common() if s not in banned)
