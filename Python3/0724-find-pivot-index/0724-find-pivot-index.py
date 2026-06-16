class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        sumRight = sum(nums)
        
        for i in range(0, len(nums)):
            sumLeft += nums[i - 1] if i > 0 else 0
            sumRight -= nums[i]
            if sumRight == sumLeft:
                return i
        
        return -1