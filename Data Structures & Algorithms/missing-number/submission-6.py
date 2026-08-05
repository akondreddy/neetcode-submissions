class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Set to determine what's in the set
        inSet = set()
        # Add to the set
        for i in range(len(nums)):
            inSet.add(nums[i])
        # Check if the number in the set
        for i in range(len(inSet)):
            if i not in inSet:
                return i
        # If the number is not in the set, the number not in nums
        # is n, which is the len(nums)
        return len(nums)