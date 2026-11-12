class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
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



