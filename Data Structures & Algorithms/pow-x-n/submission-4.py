class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Use recursion to simplify the work

        if x == 0:
            return 0
    
        isNegative = False
        
        if n < 0: 
            n = -1 * n
            isNegative = True

        def recurse(x: float, n: int):
            # Base case
            if n == 0:
                return 1
            
            # Even case, divides evenly
            if n % 2 == 0:
                half = recurse(x, n // 2)
                return half * half

            # Doesn't divide evenly for odd,
            # so multiply by additional x
            else:
                half = recurse(x, n // 2)
                return x * half * half


        result = recurse(x, n)

        if isNegative:
            return 1 / result

        return result