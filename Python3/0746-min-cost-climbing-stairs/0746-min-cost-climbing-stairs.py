class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        numStairs = len(cost)
        if numStairs < 2: return 0
        if numStairs == 2: return min(cost)

        memo = {0: cost[0], 1: cost[1]}
        for i in range(2, numStairs):
            prev_cost = min(memo[i - 1], memo[i - 2])
            memo[i] = cost[i] + prev_cost
        return min(memo[numStairs - 1], memo[numStairs - 2])