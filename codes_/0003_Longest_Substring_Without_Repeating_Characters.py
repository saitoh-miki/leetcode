# %% [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return max([unique_len(s[i:]) for i in range(len(s))], default=0)

def unique_len(s):
    n = 0
    st = set()
    for c in s:
        if c in dc:
            break
        n += 1
        st.add(c)
    return n
