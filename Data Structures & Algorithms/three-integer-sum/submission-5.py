class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        results = set()

        # Idea is to what we did in 2Sum, just again
        # Reminder to sum to 0
        for i in range(length):
            seen = set()
            first = nums[i]
            for j in range(i + 1, length):
                second = nums[j]
                leftover = -1 * (first + second)
                triple = [first, second, leftover]
                if leftover in seen:
                    triple = tuple(sorted(triple))
                    results.add(triple)
                
                seen.add(second)

        results = [list(t) for t in results]

        return results
