# %% [1313. Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/)
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums), 2):
            yield from [nums[i + 1]] * nums[i]
