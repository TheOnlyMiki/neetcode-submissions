class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        costs = [float('inf')] * n
        costs[src] = 0

        for i in range(k+1):
            new_costs = costs.copy()
            
            for from_i, to_i, price_i in flights:
                if costs[from_i] + price_i < new_costs[to_i]:
                    new_costs[to_i] = costs[from_i] + price_i

            costs = new_costs

        return costs[dst] if costs[dst] < float('inf') else -1