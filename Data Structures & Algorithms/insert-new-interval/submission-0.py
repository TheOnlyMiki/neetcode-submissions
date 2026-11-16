class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []

        for i, inter in enumerate(intervals):
            if inter[1] < newInterval[0]:
                output.append(inter)
            elif inter[0] > newInterval[1]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval = [min(inter[0], newInterval[0]), max(inter[1], newInterval[1])]

        output.append(newInterval)

        return output