class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a hashset to only start from the
        # start of a sequence
        hashset = set(nums)
        maxCounter = 0
        for num in hashset:
            # Start of sequence
            if num - 1 not in hashset:
                current = num - 1
                counter = 0
                while current + 1 in hashset:
                    counter += 1
                    current += 1
                if counter > maxCounter:
                    maxCounter = counter
        return maxCounter
            