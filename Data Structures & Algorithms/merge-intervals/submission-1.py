class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)

        intervals.sort()
        
        output = [intervals[0]]

        i = 0

        for i in range(1, n):
            pre_inter = output[-1]
            current = intervals[i]

            if pre_inter[1] < current[0]:
                output.append(current)
                continue

            output[-1][1] = max(pre_inter[1], current[1])

        return output
