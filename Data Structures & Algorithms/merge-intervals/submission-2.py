class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        max_val = max(interval[0] for interval in intervals)

        record_end = [-1] * (max_val + 1)
        for l, r in intervals:
            record_end[l] = max(record_end[l], r)

        output = []
        
        inter_start = -1
        inter_end = -1

        for i in range(len(record_end)):
            if record_end[i] != -1:
                if inter_start == -1:
                    inter_start = i

                inter_end = max(inter_end, record_end[i])

            if i == inter_end:
                output.append([inter_start, inter_end])
                inter_start, inter_end = -1, -1

        if inter_start != -1:
            output.append([inter_start, inter_end])

        return output

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
