class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = [0] * (n + 1)
        for i in range(n + 1):
            nums[i] = nums[i >> 1] + (i & 1)
        return nums