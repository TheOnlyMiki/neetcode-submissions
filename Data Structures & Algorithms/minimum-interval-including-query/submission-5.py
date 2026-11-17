class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key=lambda i:(i[0], i[1]))

        min_heap = []

        output = [0] * len(queries)

        i = 0

        for i_q, q in sorted(enumerate(queries), key=lambda i:i[1]):

            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1

                heapq.heappush(min_heap, (length, intervals[i][1]))

                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            output[i_q] = min_heap[0][0] if min_heap else -1

        return output
        
        intervals.sort(key=lambda i:(i[0], i[1]))

        output = []

        for num in queries:

            length = float('inf')

            for i in range(len(intervals)):
                if intervals[i][0] > num:
                    break

                if num <= intervals[i][1]:
                    length = min(length, intervals[i][1] - intervals[i][0] + 1)

            length = length if length < float('inf') else -1

            output.append(length)

        return output
