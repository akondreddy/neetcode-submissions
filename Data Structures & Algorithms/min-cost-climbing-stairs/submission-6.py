class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize a cache array that will memoize
        # paths that have already been explored.
        length = len(cost)
        cache = [-1] * length

        # Min cost required to reach the top
        def dfs(i):
            if i >= length:
                return 0
            if cache[i] != -1:
                return cache[i]
            oneStep = dfs(i + 1)
            twoStep = dfs(i + 2)

            minimumOption = min(oneStep, twoStep)
            cache[i] = cost[i] + minimumOption

            return cache[i]

        return min(dfs(0), dfs(1))

        
            
            