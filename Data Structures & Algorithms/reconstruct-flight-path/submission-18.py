class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        maps = defaultdict(list)

        for from_i, to_i in tickets:
            maps[from_i].append(to_i)

        for key in maps.keys():
            maps[key].sort(reverse=True)

        output = []

        def dfs(from_i):
            while maps[from_i]:
                to_i = maps[from_i].pop()
                dfs(to_i)

            output.append(from_i)

        dfs("JFK")

        return output[::-1]
        