import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        combs = []
        for comb in itertools.combinations(nums, k):
            if sum(comb) == n:
                combs.append(comb)

        return combs