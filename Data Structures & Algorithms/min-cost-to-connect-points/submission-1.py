class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        maps = defaultdict(list)

        for i in range(len(points)):
            x1,y1 = points[i]

            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                maps[i].append((distance, j))
                maps[j].append((distance, i))

        count = 0

        min_heap = [(0, 0)]

        visit = set()

        while min_heap:
            distance, point = heapq.heappop(min_heap)

            if point in visit:
                continue

            visit.add(point)
            count += distance

            for next_distance, next_point in maps[point]:
                if next_point not in visit:
                    heapq.heappush(min_heap, (next_distance, next_point))

        return count
