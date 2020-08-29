# %% [49. *Group Anagrams](https://leetcode.com/problems/group-anagrams/)
# 問題：アナグラムになる単語同士でグルーピングせよ
# 解法：文字列をソートしてタプルにして辞書のキーとする
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
