class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairsMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for char in s:
            # Scenario that char is one of the below
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            # Otherwise, char is a closing parenthesis. The pairsMap
            # checks that the most recent element element in stack is the same
            # as the value in the key pair
            else:
                if not stack or stack[-1] != pairsMap[char]:
                    return False
                stack.pop()
        
        if not stack:
            return True
        return False