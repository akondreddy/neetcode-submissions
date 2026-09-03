class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Iterate through the string using a sliding 
        # window. 

        inString = set()
        largestLen = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in inString:
                inString.add(s[right])
                right += 1
            else:
                inString.remove(s[left])
                left += 1
            if (right - left) > largestLen:
                largestLen = right - left
                
        return largestLen