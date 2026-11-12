class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for i in range(len(heights)):
            start_i = i
            while stack and stack[-1][0] > heights[i]:
                pre_h, pre_i = stack.pop()
                h = pre_h
                w = i - pre_i
                matrix = h * w
                best = max(best, matrix)
                start_i = pre_i
                

            stack.append([heights[i], start_i])

        for h, i in stack:
            best = max(best, h * (len(heights)-i))

        return best