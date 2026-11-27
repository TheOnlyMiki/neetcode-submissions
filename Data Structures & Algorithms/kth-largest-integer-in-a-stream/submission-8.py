class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        
        if len(self.min_heap) == self.size:
            heapq.heappushpop(self.min_heap, val)

        else:
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]
