class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        length = len(nums)
        for i in range(length):
            # Key: Value in the list
            # Value: Index
            numsMap[nums[i]] = i
        
        for i in range(length):
            # Retrieve value from list
            number = nums[i]
            remainder = target - number
            # If the remainder is in the dict, thus in
            # the list, and the indices aren't the same...
            if remainder in numsMap and numsMap[remainder] != i:
                if numsMap[remainder] < i:
                    return [numsMap[remainder], i]
                return [i, numsMap[remainder]]
        return []
            