class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the first index to 0, for size of n + 1
        nums = [0] * (n + 1)
        for i in range(n + 1):
            # Right shifting a number by 1 removes the least significant bit.
            # Then, i & 1 will tell us if the last bit is 1 or 0
            nums[i] = nums[i >> 1] + (i & 1)
        return nums