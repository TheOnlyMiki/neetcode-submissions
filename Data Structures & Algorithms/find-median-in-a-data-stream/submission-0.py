class MedianFinder:

    def __init__(self):
        
        self.right_min = []
        self.left_max = []

    def addNum(self, num: int) -> None:

        if self.left_max and num < -self.left_max[0]:
            heapq.heappush(self.left_max, -num)
        else:
            heapq.heappush(self.right_min, num)

        if len(self.left_max) > len(self.right_min) + 1:
            val = heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, -val)

        if len(self.right_min) > len(self.left_max) + 1:
            val = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -val)


    def findMedian(self) -> float: 

        if len(self.left_max) > len(self.right_min):
            return -self.left_max[0]
        elif len(self.left_max) < len(self.right_min):
            return self.right_min[0]
        else:
            return (self.right_min[0] - self.left_max[0]) / 2.0