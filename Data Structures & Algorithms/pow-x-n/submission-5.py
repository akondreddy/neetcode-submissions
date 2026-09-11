class Solution(object):
    def myPow(self, x, n):
        output = 1
        if n < 0:
            n = -n
            x = 1 / x
        # Use Bit Exponentiation in order to calculate power.
        # For example, if x = 7, n = 11, then 7^11 can be
        # calculated through 7^(8 + 2 + 1). In binary, can be
        # written as 1011 for the exponent.
        while n != 0:
            # Iterate through exponent in bit form
            if (n & 1):
                output *= x
            # Next power to multiply by
            x *= x
            # Next bit
            n >>= 1
        return output
            
        