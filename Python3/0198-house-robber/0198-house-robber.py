class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return nums[0]
        stack = {0: nums[0], 1: nums[1]}
        for i in range(2, len(nums)):
            el1 = stack[i-2] if i >= 2 else 0
            el2 = stack[i-3] if i >= 3 else 0
            stack[i] = max(nums[i] + el1, nums[i] + el2)
        return max(stack.values())