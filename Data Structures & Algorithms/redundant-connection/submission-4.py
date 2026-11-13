class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]
        size = [1] * len(parent)

        def find(i):
            boss = i
            while parent[boss] != boss:
                boss = parent[boss]

            while parent[i] != boss:
                parent[i], i = boss, parent[i]

            return boss

        def union(a,b):
            boss_a, boss_b = find(a), find(b)

            if boss_a == boss_b:
                return True

            if size[boss_a] < size[boss_b]:
                boss_a, boss_b = boss_b, boss_a
            parent[boss_b] = boss_a
            size[boss_a] += size[boss_b]

            return False

        for a, b in edges:
            if union(a, b):
                return [a, b]

        return [-1, -1]







































        
        n = len(edges) + 1
        parent = [i for i in range(n)]
        size = [1] * n

        def find_boss(i):
            boss = i
            while parent[boss] != boss:
                boss = parent[boss]

            while parent[i] != boss:
                i, parent[i] = parent[i], boss

            return boss

        def union(a, b):
            boss_a, boss_b = find_boss(a), find_boss(b)

            if boss_a == boss_b:
                return True

            if size[boss_a] < size[boss_b]:
                boss_a, boss_b = boss_b, boss_a
            parent[boss_b] = boss_a
            size[boss_a] += size[boss_b]

            return False

        for a, b in edges:
            if union(a, b):
                return [a, b]

        return [-1, -1]
