class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 1
        j = k - 1
        maxAvg = float('-inf')
        summation = sum([x for x in nums[:k]])
        maxAvg = summation / k
        while i <= len(nums) - k:
            j = i + k - 1
            summation = summation + nums[j] - nums[i - 1]
            print(summation)
            maxAvg = max(maxAvg, summation / k)
            i += 1

        return maxAvg
        