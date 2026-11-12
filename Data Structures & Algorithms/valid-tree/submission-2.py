class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        parent = [i for i in range(n)]
        size = [1] * n
        
        def find(i):
            boss = i
            while parent[boss] != boss:
                boss = parent[boss]

            while parent[i] != boss:
                parent[i], i = boss, parent[i]

            return boss

        def union(a, b):
            boss_a, boss_b = find(a), find(b)

            if boss_a == boss_b:
                return False

            if size[boss_a] < size[boss_b]:
                boss_a, boss_b = boss_b, boss_a

            parent[boss_b] = boss_a
            size[boss_a] += size[boss_b]

            return True

        for a, b in edges:
            if union(a, b) is False:
                return False

        return True
        