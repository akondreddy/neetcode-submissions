class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            integer = nums[middle]
            if integer == target:
                return middle
            if target < integer:
                right = middle - 1
            if target > integer:
                left = middle + 1
        return -1

        