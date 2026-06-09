class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        trailing_zeros = 0
        while i < len(nums) - trailing_zeros:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                trailing_zeros += 1
            else:
                i += 1
        