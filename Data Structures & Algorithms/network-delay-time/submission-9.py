class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist = [float('inf')] * (n+1)
        dist[0] = 0
        dist[k] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        max_dist = max(dist)

        return max_dist if max_dist < float('inf') else -1
        
        maps = [[] for i in range(n+1)]

        for u, v, t in times:
            maps[u].append((t, v))

        min_heap = maps[k]
        
        heapq.heapify(min_heap)

        visit = {k:0}

        while min_heap:
            t, v = heapq.heappop(min_heap)

            if v not in visit:
                visit[v] = t

                for next_t, next_v in maps[v]:
                    if next_v not in visit:
                        heapq.heappush(min_heap, (t + next_t, next_v))

        if len(visit) != n:
            return -1

        return max(visit.values())

