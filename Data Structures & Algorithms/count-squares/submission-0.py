class CountSquares:

    def __init__(self):
        self.point = []
        self.count_point = defaultdict(int)

    def add(self, point: List[int]) -> None:

        self.count_point[(point[0], point[1])] += 1

        self.point.append((point[0], point[1]))
        

    def count(self, point: List[int]) -> int:
        
        px, py = point[0], point[1]

        count = 0

        for x, y in self.point:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue

            count += self.count_point[(x, py)] * self.count_point[(px, y)]

        return count
