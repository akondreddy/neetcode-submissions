class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min-heap: Storing elements to keep
        # smallest at top. After that, the largest
        # element is the smallest element among
        # top k largest.

        return heapq.nlargest(k, nums)[-1]

