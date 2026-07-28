class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        fromEnd = len(digits) - 1
        
        digits[fromEnd] += 1
        if digits[fromEnd] != 10:
            return digits
        
        while fromEnd > 0 and digits[fromEnd] == 10:
            digits[fromEnd] = 0
            digits[fromEnd - 1] += 1
            fromEnd -= 1
        
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)

        return digits