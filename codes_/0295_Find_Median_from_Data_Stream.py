# %% [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
class MedianFinder(list):
    def addNum(self, num):
        self.insert(bisect.bisect_left(self, num), num)

    def findMedian(self) -> float:
        if (n := len(self)) % 2:
            return self[n // 2]
        return (self[n // 2 - 1] + self[n // 2]) / 2
