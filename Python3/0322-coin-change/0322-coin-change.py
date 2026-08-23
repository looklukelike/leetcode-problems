class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amt):
            if amt == 0 :
                return 0
            elif amt < 0:
                return float('inf')
            
            if amt in memo:
                return memo[amt]
            else:
                best = float('inf')
                for coin in coins:
                    best = min(
                        best,
                        1 + dp(amt - coin)
                    )

                memo[amt] = best

            return memo[amt]

        res = dp(amount)
        return res if res <= amount else -1
