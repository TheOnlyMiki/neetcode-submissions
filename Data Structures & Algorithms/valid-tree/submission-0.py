class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False
        
        maps = [[] for i in range(n)]

        for a,b in edges:
            maps[a].append(b)
            maps[b].append(a)

        level = [0]

        visit = {0}

        while level:
            next_level = []

            for node in level:
                for next_node in maps[node]:

                    if next_node not in visit:
                        visit.add(next_node)
                        next_level.append(next_node)

            level = next_level

        return len(visit) == n
        