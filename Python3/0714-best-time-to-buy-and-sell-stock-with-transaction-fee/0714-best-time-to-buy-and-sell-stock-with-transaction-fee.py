class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        hold = [0] * n
        cash = [0] * n

        hold[0] = - prices[0]
        cash[0] = 0

        for i in range(1, n):
            
            # get the best of doing nothing or buy today
            hold[i] = max(
                hold[i - 1],                        # hold / do nothing
                cash[i - 1] - prices[i]             # buy today
            )
            
            # get the best of holding or selling today
            cash[i] = max(
                cash[i - 1],                        # hold / do nothing
                hold[i - 1] + prices[i] - fee       # sell today
            )

        return max(cash[n - 1], hold[n - 1])