class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Brute force solution
        # Sort through the array, and on each pass
        # take the largest two stones.
        if len(stones) == 1:
            return stones[0]
        sortedArray = sorted(stones)
        while len(sortedArray) > 1:
            sortedArray[-1] -= sortedArray[-2]
            if sortedArray[-1] == 0:
                del sortedArray[-1]
                del sortedArray[-1]
            else:
                del sortedArray[-2]
            sortedArray = sorted(sortedArray)

        if not sortedArray:
            return 0
        return sortedArray[0]
        