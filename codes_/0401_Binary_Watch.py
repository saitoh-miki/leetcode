# %% [401. Binary Watch](https://leetcode.com/problems/binary-watch/)
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for a in itertools.combinations(range(10), num):
            bits = [0] * 10
            for i in a:
                bits[i] = 1
            h = sum(bits[i] * 2 ** i for i in range(4))
            if h < 12:
                m = sum(bits[i + 4] * 2 ** i for i in range(6))
                if m < 60:
                    res.append(f"{h}:{m:02}")
        return res
