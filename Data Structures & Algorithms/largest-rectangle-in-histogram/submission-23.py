class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Method 2 - stack
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

        # Method 1 - stack
        stack = []

        best = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i

                best = max(best, h * w)
                
            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            
            if stack:
                w = len(heights) - stack[-1] - 1
            else:
                w = len(heights)

            best = max(best, h * w)

        return best