class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        inSet = set()
        for i in range(len(nums)):
            inSet.add(nums[i])
        for i in range(len(inSet)):
            if i not in inSet:
                return i
        return len(nums)