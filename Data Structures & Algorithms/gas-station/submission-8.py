class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start, end = len(gas)-1, 0

        tank = gas[start] - cost[start]

        while start > end:
            if tank < 0:
                start -= 1
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1

        return start if tank >= 0 else -1









































        start, end = len(gas)-1, 0
        tank = gas[start] - cost[start]

        while start > end:
            if tank < 0:
                start -= 1
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1

        return start if tank >= 0 else -1
        
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        index = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                index = i+1

        return index
            
