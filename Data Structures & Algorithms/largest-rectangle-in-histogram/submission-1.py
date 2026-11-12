class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Method 1 - slide window
        stack = []

        best = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i
                if stack:
                    w = i - stack[-1] - 1

                best = max(best, h * w)
                
            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            w = len(heights)
            if stack:
                w = len(heights) - stack[-1] - 1

            best = max(best, h * w)

        return best