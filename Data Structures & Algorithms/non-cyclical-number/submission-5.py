class Solution:
    def isHappy(self, n: int) -> bool:
        def sum(n: int) -> int:
            total = 0
            while n > 0:
                num = n % 10
                total += num * num
                n = n // 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            total = sum(n)
            seen.add(n)
            if total == 1:
                return True
            else:
                n = total
        return n == 1
            