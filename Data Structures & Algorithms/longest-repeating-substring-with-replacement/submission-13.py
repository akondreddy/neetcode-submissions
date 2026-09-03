class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        result = 0

        left = maxf = 0
        for right in range(len(s)):
            # If the char exists, then add 1 to it,
            # otherwise, set it to 0, then add 1
            frequency[s[right]] = frequency.get(s[right], 0) + 1  
            maxf = max(maxf, frequency[s[right]])

            while (right - left + 1) - maxf > k:
                frequency[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result
        