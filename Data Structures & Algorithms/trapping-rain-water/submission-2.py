class Solution:
    def trap(self, height: List[int]) -> int:
        # Method 1 - dynamic program
        '''n = len(height)

        left_h_max = [0] * n
        left_h_max[0] = height[0]

        right_h_max = [0] * n
        right_h_max[n-1] = height[n-1]
        
        # from left to right:
        for i in range(1, n):
            left_h_max[i] = max(left_h_max[i-1], height[i])

        # from right to left:
        for i in range(n-2, -1, -1):
            right_h_max[i] = max(right_h_max[i+1], height[i])

        count = 0
        # compute the gaps
        for i in range(n):
            count += min(left_h_max[i], right_h_max[i]) - height[i]

        return count'''
        # time complexity O(n), space complexity O(n)

        # Method 2 - Stack
        n = len(height)

        stack = []

        i = 0
        count = 0

        while i < n:
            # Stack not empty and current column higher than last wall in stack
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                # Take the info out from the stack then pop out
                last_wall_i = stack[-1]
                stack.pop()

                # 当前位置往前没有能接水的
                if len(stack) == 0:
                    break

                # 距离等于当前位置减去移除后的最后一列的位置。该距离可用于重新计算上一道墙体高度与当前位置之间缺失的部分。
                distance = i - stack[-1] - 1
                # 计算当前墙和之前的墙之间的缺失部分
                min_h = min(height[i], height[stack[-1]])
                count += distance * (min_h - height[last_wall_i])

            stack.append(i)
            #Move to next index
            i += 1

        return count
