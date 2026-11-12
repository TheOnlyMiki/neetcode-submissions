class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []

        for i in range(k):
            heapq.heappush(distances, (-(points[i][0]**2 + points[i][1]**2), i))

        for i in range(k, len(points)):
            distance = -(points[i][0]**2 + points[i][1]**2)

            if distance > distances[0][0]:
                heapq.heappushpop(distances, (distance, i))

        output = []

        for _, i in distances:
            output.append(points[i])

        return output