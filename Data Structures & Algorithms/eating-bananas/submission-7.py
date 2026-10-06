class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Use a binary search to check options
        left = 1
        right = max(piles)
        smallestSpeed = right

        while left <= right:
            mid = (left + right) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)
            if totalTime <= h:
                smallestSpeed = mid
                right = mid - 1
            else:
                left = mid + 1
        return smallestSpeed