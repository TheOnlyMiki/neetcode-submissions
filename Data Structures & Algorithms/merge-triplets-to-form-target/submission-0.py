class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        triplets.sort()
        current = [0, 0, 0]
        
        for i in range(3):
            for triplet in triplets:
                if triplet[i] == target[i]:
                    current = [max(current[0], triplet[0]), max(current[1], triplet[1]), max(current[2], triplet[2])]
                    break

        return current == target