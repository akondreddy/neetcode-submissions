class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        results = []

        # Idea is to what we did in 2Sum, just again
        # Reminder to sum to 0
        for i in range(length):
            seen = set()
            for j in range(i + 1, length):
                first = nums[i]
                second = nums[j]
                leftover = -1 * (first + second)
                
                if leftover in seen:
                    triple = [first, second, leftover]
                    triple = sorted(triple)
                    if triple not in results:
                        results.append(triple)
                
                seen.add(second)

            seen.add(first)
        return results