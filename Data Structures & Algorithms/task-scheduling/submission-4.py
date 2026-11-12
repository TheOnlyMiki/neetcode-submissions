class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = defaultdict(int)

        for task in tasks:
            count[task] += 1

        count = [ -val for val in count.values() ]

        heapq.heapify(count)

        cooling = deque()

        cycles = 0

        while count or cooling:
            if cooling and cooling[0][1] < cycles:
                remain, times = cooling.popleft()
                heapq.heappush(count, remain)

            if count:
                remain = heapq.heappop(count) + 1
                if remain != 0:
                    cooling.append((remain, cycles + n))

            cycles += 1

        return cycles