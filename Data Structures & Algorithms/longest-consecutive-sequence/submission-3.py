class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Could handle this by sorting first
        if (len(nums) == 0):
            return 0
        counter = 1
        maxCounter = counter
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 1):
            if (sortedNums[i] + 1 == sortedNums[i + 1]):
                counter += 1
            elif (sortedNums[i]== sortedNums[i + 1]):
                counter += 0
            else:
                counter = 1
            if (counter > maxCounter):
                maxCounter = counter
        return maxCounter