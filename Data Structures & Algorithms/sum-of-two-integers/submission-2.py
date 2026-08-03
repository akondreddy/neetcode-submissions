class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Use the mask to restrict Python to 32 bits
        mask = 0xFFFFFFFF
        # This is the max positive signed integer
        max_int = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a ^ mask)