class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        count = 0

        pre_inter = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < pre_inter[1]:
                count += 1
                pre_inter = intervals[i] if pre_inter[1] > intervals[i][1] else pre_inter
            else:
                pre_inter = intervals[i]

        return count
                
