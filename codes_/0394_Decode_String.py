# %% [394. Decode String](https://leetcode.com/problems/decode-string/)

class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = re.sub(r'(\d+)\[([^[]+?)\]', subfunc, s)
        return s

def subfunc(m):
    return m.group(2) * int(m.group(1))
