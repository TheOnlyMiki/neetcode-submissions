class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Method 1 - slide window
        stack = []

        best = 0

        for i in range(len(heights)+1):
            while stack and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                h = heights[stack.pop()]
                w = i
                if stack:
                    w = i - stack[-1] - 1

                best = max(best, h * w)
                
            stack.append(i)

        return best