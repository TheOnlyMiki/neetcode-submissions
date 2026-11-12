class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        best = 0

        for i, h in enumerate(heights):
            start_i = i
            while stack and stack[-1][1] > h:
                pre_i, pre_h = stack.pop()
                best = max(best, (i - pre_i) * pre_h)
                start_i = pre_i

            stack.append([start_i, h])
            #print(stack)

        for i, h in stack:
            best = max(best, (len(heights) - i) * h)

        return best