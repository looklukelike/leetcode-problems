class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0 for _ in range(n + 1)]
        
        dp[0] = costs[0] + 1
        
        if n > 1:
            dp[1] = min(
                costs[1] + 2**2,
                dp[0] + costs[1] + 1**2,
            )
        if n > 2:
            dp[2] = min(
                dp[1] + costs[2],
                costs[2] + 3**2
            )
        
        for j in range(2, n):
            dp[j] = min(
                dp[j - 1] + costs[j] + 1**2,
                dp[j - 2] + costs[j] + 2**2,
                dp[j - 3] + costs[j] + 3**2
            ) 


        return dp[n - 1]