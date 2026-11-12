class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
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

