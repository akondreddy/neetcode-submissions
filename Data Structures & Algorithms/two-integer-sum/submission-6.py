class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        hashtable = {}

        for i in range(length):
            leftover = target - nums[i]
            if leftover in hashtable:
                return [hashtable[leftover], i]
            hashtable[nums[i]] = i
        
        return []