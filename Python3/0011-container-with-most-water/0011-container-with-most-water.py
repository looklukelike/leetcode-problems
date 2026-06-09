class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        x1 = 0
        x2 = len(height) - 1
        while x1 < x2:
            y = min(height[x1], height[x2])
            a = (x2 - x1) * y
            area = a if a > area else area
            if height[x1] > height[x2]:
                x2 -= 1
            else:
                x1 +=1

        return area