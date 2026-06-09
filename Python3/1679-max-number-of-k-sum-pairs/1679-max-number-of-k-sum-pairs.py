class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = dict()
        operations = 0

        for val in nums:
            d[val] = d.get(val, 0) + 1

        for a in d:
            if (k - a) in d:
                operations += min(d[a], d[k-a]) 
        
        return operations // 2