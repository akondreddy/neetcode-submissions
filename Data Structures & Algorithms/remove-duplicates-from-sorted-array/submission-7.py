class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        k = 1
        duplicated = nums[0]
        for i in range(length):
            # Curernt number we check against
            currentNum = nums[i]
            if currentNum != duplicated:
                # Assign the next 
                nums[k] = currentNum
                duplicated = currentNum
                k += 1

        return k
