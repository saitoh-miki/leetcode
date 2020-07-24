# %% [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for num in nums:
            if num in st:
                return True
            st.add(num)
        return False
