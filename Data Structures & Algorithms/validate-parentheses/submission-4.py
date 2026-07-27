class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairsMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for char in s:
            # Check if char is a closing parenthesis. The pairsMap
            # checks that the most recent element element in stack is the same
            # as the value in the key pair
            if char in pairsMap:
                if not stack or stack[-1] != pairsMap[char]:
                    return False
                stack.pop()
            # Scenario that char is value in pairsMap
            else:
                stack.append(char)
        
        return not stack