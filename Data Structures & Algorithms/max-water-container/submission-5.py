class Solution:
    def maxArea(self, heights: List[int]) -> int:

        best = 0

        l, r = 0, len(heights)-1

        while l < r:
            distance = r - l
            min_height = min(heights[l], heights[r])
            sums = distance * min_height

            best = max(best, sums)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return best
        