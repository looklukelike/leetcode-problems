class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        solution = []

        for spell in spells:
            count = 0
            lo = 0 
            hi = len(potions)
            mid = lo + hi // 2
            while lo <= hi - 1:
                strength = spell * potions[mid]
                if strength >= success:
                    count += hi - mid 
                    hi = mid
                else:
                    lo = mid + 1
                mid = (lo + hi) // 2

            solution.append(count)

        return solution