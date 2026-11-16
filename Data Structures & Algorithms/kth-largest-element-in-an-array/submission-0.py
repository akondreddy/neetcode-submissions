class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute force: Sort then pick the kth largest
        sortedList = sorted(nums)
        return sortedList[len(nums) - k]