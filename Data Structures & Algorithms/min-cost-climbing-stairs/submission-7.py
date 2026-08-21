class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Modify the array: each step in cost
        # represents the min cost to reach the top
        # starting from the step i. 
        for i in range(len(cost) - 3, -1, -1):
            # Pay cost at this step then the cheaper
            # of the two available ones
            cost[i] += min(cost[i + 1], cost[i + 2])
        # Start from the cheaper step
        return min(cost[0], cost[1])