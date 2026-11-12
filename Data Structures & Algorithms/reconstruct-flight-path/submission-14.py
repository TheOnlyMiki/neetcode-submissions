class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # 反向遍历

        output = []
        edges = defaultdict(list)

        for src, dst in tickets:
            edges[src].append(dst)
        
        for values in edges.values():
            values.sort(reverse=True)

        s = ["JFK"]
        cur = "JFK"

        while s:
            cur = s[-1]

            if edges[cur]:
                s.append(edges[cur].pop())
            else:
                output.append(s.pop())

        return output[::-1]

        # DFS - last out (反向遍历)

        maps = defaultdict(list)

        for from_i, to_i in sorted(tickets, reverse=True):
            maps[from_i].append(to_i)

        path = []

        def dfs(from_i):
            while maps[from_i]:
                to_i = maps[from_i].pop()
                dfs(to_i)

            path.append(from_i)

        dfs("JFK")

        return path[::-1]
        
        # Backtrack

        maps = defaultdict(list)

        for from_i, to_i in sorted(tickets):
            maps[from_i].append([to_i, False])

        n = len(tickets)

        path = ["JFK"]

        def backtrack(from_i):
            if len(path) == n+1:
                return True

            for i, (to_i, visit) in enumerate(maps[from_i]):
                if visit:
                    continue

                # 删掉的话不影响结果，但是去重能稍微减少一些分支
                if i > 0 and to_i == maps[from_i][i-1][0] and not maps[from_i][i-1][1]:
                    continue

                path.append(to_i)
                maps[from_i][i][1] = True

                if backtrack(to_i):
                    return True

                maps[from_i][i][1] = False
                path.pop()

            return False


        backtrack("JFK")

        return path
