class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        union = nums1.intersection(nums2)

        result = [[], []]
        for x in nums1:
            if x not in union:
                result[0].append(x)

        for x in nums2:
            if x not in union:
                result[1].append(x)

        return result
        
