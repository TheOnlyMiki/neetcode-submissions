class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        good = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i, v in enumerate(triplet):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3

        triplets.sort()
        current = [0, 0, 0]
        
        for i in range(3):
            for triplet in triplets:
                if triplet[i] == target[i]:
                    current = [max(current[0], triplet[0]), max(current[1], triplet[1]), max(current[2], triplet[2])]
                    break

        return current == target