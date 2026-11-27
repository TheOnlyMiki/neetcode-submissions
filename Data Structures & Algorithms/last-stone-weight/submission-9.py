class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []

        for num in stones:
            heapq.heappush(max_heap, -num)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) * -1
            stone2 = heapq.heappop(max_heap) * -1

            remain = stone1 - stone2
            if remain != 0:
                heapq.heappush(max_heap, -remain)

        return -max_heap[0] if max_heap else 0