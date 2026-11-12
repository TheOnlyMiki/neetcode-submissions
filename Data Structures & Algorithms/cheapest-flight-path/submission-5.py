class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        edge = k + 1

        costs = [float('inf')] * n
        costs[src] = 0

        for i in range(edge):
            print(costs)
            pre_costs = costs.copy()

            for from_i, to_i, price in flights:
                if pre_costs[from_i] + price < costs[to_i]:
                    costs[to_i] = pre_costs[from_i] + price

                #costs = pre_costs

        return costs[dst] if costs[dst] < float('inf') else -1

