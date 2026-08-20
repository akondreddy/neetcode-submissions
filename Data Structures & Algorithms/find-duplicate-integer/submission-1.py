class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute force, iterate through array with 
        # hashset
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return nums[i]
            else:
                hashset.add(nums[i])
        return -1