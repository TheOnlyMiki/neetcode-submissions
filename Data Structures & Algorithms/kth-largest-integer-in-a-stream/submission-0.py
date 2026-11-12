class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.min_heap = []
        self.k = k

        for num in nums:
            if self.k != len(self.min_heap):
                heapq.heappush(self.min_heap, num)
            elif num > self.min_heap[0]:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)

        return
        

    def add(self, val: int) -> int:
        if self.k != len(self.min_heap):
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]
