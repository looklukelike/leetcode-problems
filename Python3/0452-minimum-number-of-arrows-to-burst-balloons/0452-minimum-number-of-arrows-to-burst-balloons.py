class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        shots = 1
        prev_start, prev_end = points[0]
        for i in range(1, len(points)):
            start, end = points[i]

            if start <= prev_end:
                continue
            else:
                shots += 1
                prev_end = end

            prev_start = start
            prev_end = min(prev_end, end)

        return shots