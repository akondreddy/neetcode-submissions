class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        length = len(nums)

        for i in range(length):
            value = nums[i]
            if value in seen:
                return True
            else:
                seen.add(value)
        
        return False