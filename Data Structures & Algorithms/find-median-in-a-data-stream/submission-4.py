class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:

        if self.left_max_heap and -self.left_max_heap[0] < num:
            heapq.heappush(self.right_min_heap, num)
        else:
            heapq.heappush(self.left_max_heap, -num)

        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            num = heapq.heappop(self.left_max_heap) * -1

            heapq.heappush(self.right_min_heap, num)

        elif len(self.left_max_heap) + 1 < len(self.right_min_heap):
            num = heapq.heappop(self.right_min_heap)

            heapq.heappush(self.left_max_heap, -num)

    def findMedian(self) -> float:
        
        if len(self.left_max_heap) > len(self.right_min_heap):
            return -self.left_max_heap[0]

        elif len(self.left_max_heap) < len(self.right_min_heap):
            return self.right_min_heap[0]

        else:
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2.0
        