class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        longest = max(s, t)
        for char in set(longest):
            if s.count(char) != t.count(char):
                return False
        return True