class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = max(piles)

        left, right = 1, k
        best_k = k

        while left <= right:
            k = (left + right) // 2
            cur_h = 0
            for pile in piles:
                cur_h += math.ceil(pile / k)

            if cur_h > h:
                left = k + 1
            else:
                best_k = k
                right = k - 1

        return best_k