class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Use the prefix/suffix method.
        # Compute all products before the element
        # and all elements after it

        length = len(nums)

        stored = [0] * length
        prefix = [0] * length
        suffix = [0] * length

        # Nothing is left of the 0th index
        prefix[0] = 1
        # Nothing is right of the last index
        suffix[length - 1] = 1

        for i in range(1, length):
            # Compute the new prefix
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(length - 2, -1, -1):
            # Compute the new suffix, working backwards
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(length):
            stored[i] = prefix[i] * suffix[i]
        return stored
