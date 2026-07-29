class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to compute the square
        # of digits
        def sum(n: int) -> int:
            total = 0
            while n > 0:
                num = n % 10
                total += num * num
                n = n // 10
            return total

        # Set for what numbers have been seen to avoid
        # loops not ending
        seen = set()
        while n != 1 and n not in seen:
            total = sum(n)
            seen.add(n)
            if total == 1:
                return True
            else:
                n = total
        return n == 1
            