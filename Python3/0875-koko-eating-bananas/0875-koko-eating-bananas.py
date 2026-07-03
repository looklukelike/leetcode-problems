import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(k):
            tot_sum = sum((pile + k -1) // k for pile in piles)
            return tot_sum <= h

        lo, hi = 1, max(piles)

        while lo <= hi:
            k = (lo + hi) // 2
            if can_eat(k):
                hi = k - 1
            else:
                lo = k + 1

        return lo
        
