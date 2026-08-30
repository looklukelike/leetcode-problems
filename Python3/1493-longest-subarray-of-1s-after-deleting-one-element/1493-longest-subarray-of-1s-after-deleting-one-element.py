class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        start = 0
        end = 1

        max_len = 0
        curr_len = 0
        while end < len(nums):
            if nums[end] == 1:
                end += 1
            else:
                new_len = end - start - (nums[start] == 0)
                max_len = max(max_len, new_len + curr_len)
                curr_len = new_len

                start = end
                end += 1

        return max_len if max_len < len(nums) - 1 else max_len - 1
