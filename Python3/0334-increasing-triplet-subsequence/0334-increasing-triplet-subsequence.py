import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        heap = [sys.maxsize, sys.maxsize]

        if len(nums) < 3 or len(set(nums)) < 3:
            return False
        
        for i in range(0, len(nums) - 1 - 1):
            if nums[i] == heap[0]:
                continue
            heap[0] = nums[i]
            for k in range(len(nums) - 1, i + 1, -1):
                if nums[i] > nums[k] or nums[k] == heap[1]:
                    continue
                heap[1] = nums[1]
                for j in range(i + 1, k):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False