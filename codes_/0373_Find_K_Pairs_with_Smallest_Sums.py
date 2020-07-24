# %% [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        ans = []
        for i in nums1:
            if len(ans) >= k and ans[k - 1][0] <= i + nums2[0]:
                break
            for j in nums2:
                ans.insert(bisect.bisect(ans, (i + j, 2 ** 32 - 1)), (i + j, i))
        return [(i[1], i[0] - i[1]) for i in ans[:k]]
