class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        
        min_heap = [(grid[0][0], 0, 0)]
        visit = {(0, 0)}

        while min_heap[0][1] != m-1 or min_heap[0][2] != n-1:
            height, i, j = heapq.heappop(min_heap)
            
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+a, j+b

                if 0 <= x < m and 0 <= y < n and (x, y) not in visit:
                    visit.add((x,y))
                    heapq.heappush(min_heap, (max(height, grid[x][y]), x, y))
        
        return min_heap[0][0]
