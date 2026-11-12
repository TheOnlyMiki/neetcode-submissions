class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        
        maps = {i:[] for i in range(n)}

        min_heap = []

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i+1, n):
                x2,y2 = points[j]

                distance = abs(x1-x2) + abs(y1-y2)

                maps[i].append((distance, j))
                maps[j].append((distance, i))

        count = 0

        visit = set()

        min_heap = [(0, 0)]

        while len(visit) < n:
            cost, point = heapq.heappop(min_heap)

            if point in visit:
                continue

            count += cost
            visit.add(point)

            for cost, next_point in maps[point]:
                if next_point not in visit:
                    heapq.heappush(min_heap, (cost, next_point))

        return count
                
        