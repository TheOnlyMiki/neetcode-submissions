class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        size = [1] * n

        def find(i):
            boss = i
            while parent[boss] != boss:
                boss = parent[boss]

            while parent[i] != boss:
                next_parent = parent[i]
                parent[i] = boss
                i = next_parent

            return boss

        self.bosses = n

        def union(a, b):
            boss_a, boss_b = find(a), find(b)

            if boss_a == boss_b:
                return False

            self.bosses -= 1

            if size[boss_a] < size[boss_b]:
                boss_a, boss_b = boss_b, boss_a

            parent[boss_b] = boss_a
            size[boss_a] += boss_b

            return True

        for a, b in edges:
            union(a, b)

        output = 0
        for i, boss in enumerate(parent):
            if i == boss:
                output += 1
        
        return self.bosses
