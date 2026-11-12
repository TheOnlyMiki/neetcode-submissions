class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [0]

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) != 1:
            stone_1 = heapq.heappop(max_heap)
            stone_2 = heapq.heappop(max_heap)

            remain = stone_2 - stone_1

            if remain != 0:
                heapq.heappush(max_heap, -remain)

        return abs(max_heap[0])