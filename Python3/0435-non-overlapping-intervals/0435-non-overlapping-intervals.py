class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1]) # sort interval by end_time
        # [1,2] [2,3] [1,3] [2,3] [1, 4]
        counter = -1
        prev_end_time = intervals[0][1]

        for interval in intervals:
            start_time, end_time = interval

            if start_time >= prev_end_time:
                prev_end_time = end_time
            else:
                counter += 1

        return counter

            