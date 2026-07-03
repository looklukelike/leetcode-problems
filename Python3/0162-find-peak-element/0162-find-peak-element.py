class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        for i in range(1, len(nums) - 1):
            gtr_left = nums[i] > nums[i - 1]
            gtr_right = nums[i] > nums[i + 1]
            if gtr_left and gtr_right:
                return i

        if nums[i + 1] > nums[i]:
            return i + 1
        