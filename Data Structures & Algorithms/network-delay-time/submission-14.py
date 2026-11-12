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
        
        maps = defaultdict(list)

        for u, v, t in times:
            maps[u].append((t, v))

        min_heap = [(0, k)]

        visit = set()

        while min_heap:
            t, v = heapq.heappop(min_heap)

            if v in visit:
                continue

            visit.add(v)

            if len(visit) == n:
                return t

            for next_t, next_v in maps[v]:
                if next_v not in visit:
                    heapq.heappush(min_heap, (t + next_t, next_v))

        return -1



