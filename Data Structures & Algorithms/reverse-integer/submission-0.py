class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        # Boundaries
        MAX = pow(2, 31) - 1
        MIN = -pow(2, 31)
        num = x
        # Handle negative scenarios
        isNeg = False
        if num < 0:
            isNeg = True
        if isNeg:
            num = -num
        # Iterate through the entire integer
        while num != 0:
            digit = num % 10
            # Within bounds
            if result > MAX // 10 or result < MIN // 10:
                return 0
            # Ensuring not overflowing
            if result == MAX // 10 and digit > MAX % 10:
                return 0
            # Ensuring not underflowing
            if result == MIN // 10 and digit < MIN % 10:
                return 0
            result = result * 10 + digit
            # Return an int, not float
            num //= 10
        if isNeg == False:
            return result
        return -result
