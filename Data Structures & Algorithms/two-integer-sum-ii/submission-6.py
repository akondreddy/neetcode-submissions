class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Let's try a two-pointer algorithm
        # Already sorted in non-decreasing order

        left = 0
        right = len(numbers) - 1

        while left < right:
            summed = numbers[left] + numbers[right]
            if summed > target:
                right -= 1
            elif summed < target:
                left += 1
            elif summed == target:
                return [left + 1, right + 1]
        
        return []