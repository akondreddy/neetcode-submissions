class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # 32 bit integer
        for i in range(32):
            # Creates a mask based off of the i-th index.
            # For the first loop, we do 1 << 0, which yields a 32 bit int,
            # where only the end is 1. Say it was a 4 bit int, then it would
            # look like 0001. Then for the second iteration, it would be 
            # 0010. 
            mask = 1 << i
            # Using the AND operator determines whether the bit is set or not.
            # So long as it's greater than 0, then the bit was set
            if (mask & n) > 0:
                count += 1
        return count