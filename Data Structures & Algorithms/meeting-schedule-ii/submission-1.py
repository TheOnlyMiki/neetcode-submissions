"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda i:(i.start, i.end))

        min_heap = []

        for i in range(len(intervals)):

            while min_heap and min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)
                break
            
            heapq.heappush(min_heap, intervals[i].end)

        return len(min_heap)










































        
        intervals.sort(key=lambda i: i.start)

        rooms_end_time_min_heap = []

        for inter in intervals:
            if rooms_end_time_min_heap and inter.start >= rooms_end_time_min_heap[0]:
                heapq.heappop(rooms_end_time_min_heap)

            heapq.heappush(rooms_end_time_min_heap, inter.end)

        return len(rooms_end_time_min_heap)
