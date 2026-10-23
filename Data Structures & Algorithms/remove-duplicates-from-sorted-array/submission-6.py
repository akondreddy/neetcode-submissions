class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Already in non-decreasing order
        hashset = set()
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] in hashset:
                del nums[i]
                length -= 1
            else:
                hashset.add(nums[i])
                i += 1
        return length