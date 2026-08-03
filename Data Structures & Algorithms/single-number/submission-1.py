class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # The key reasoning is using bitwise XOR, ^,
        # operator. Any number ^ itself, say 7 ^ 7 = 0. 
        # This means, by iterating through the entire
        # array and performing XOR operation, the one
        # number that has no dupes will perform 
        # num ^ 0 = num. 0 ^ 0 = 0. 
        num = 0
        for i in range(len(nums)):
            num = num ^ nums[i]
        return num 
        