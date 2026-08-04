class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):
            # Yields the bit based off i-th position
            bit = (n >> i) & 1
            # Add the bit to the corresponding mirrored position
            reverse += (bit << (31 - i))
        return reverse