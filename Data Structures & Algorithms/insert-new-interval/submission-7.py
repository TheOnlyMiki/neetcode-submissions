class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)

        output = []

        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1

        output.append(newInterval)

        if i < n:
            output += intervals[i:]

        return output

        













































        n = len(intervals)
        
        output = []

        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1

        output.append(newInterval)

        if i < n:
            output += intervals[i:]

        return output
        
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