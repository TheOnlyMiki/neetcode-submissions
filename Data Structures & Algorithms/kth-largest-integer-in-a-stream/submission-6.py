class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        
        if self.k > len(self.min_heap):
            heapq.heappush(self.min_heap, val)

        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)

        return self.min_heap[0]