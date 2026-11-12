class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        best = 0
        while l < r:
            min_h = min(heights[l], heights[r])
            distance = r - l
            cur = min_h * distance

            if cur > best:
                best = cur

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return best