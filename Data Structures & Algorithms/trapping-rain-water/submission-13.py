class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n-1
        left_h_max = height[left]
        right_h_max = height[right]

        count = 0

        while left < right:
            if left_h_max < right_h_max:
                left += 1
                left_h_max = max(left_h_max, height[left])
                count += left_h_max - height[left]
            else:
                right -= 1
                right_h_max = max(right_h_max, height[right])
                count += right_h_max - height[right]

        return count

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
        '''n = len(height)

        stack = []

        i = 0
        count = 0

        for i in range(n):
            # Stack not empty and current column higher than last wall in stack
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                # Take the info out from the stack then pop out
                last_wall_h = height[stack.pop()]

                # 当前位置往前没有能接水的
                if len(stack) == 0:
                    break

                # 距离等于当前位置减去移除后的最后一列的位置。该距离可用于重新计算上一道墙体高度与当前位置之间缺失的部分。
                distance = i - stack[-1] - 1
                # 计算当前墙和之前的墙之间的缺失部分
                min_h = min(height[i], height[stack[-1]])
                count += distance * (min_h - last_wall_h)

            stack.append(i)

        return count'''
        # time complexity O(n), space complexity O(n)

        # Method 3 - two pointer
        l, r = 0, len(height)-1

        count = 0

        left_max = height[l]
        right_max = height[r]

        while l < r:
            # 如果右边有比左边高，计算左边的积水
            if left_max < right_max:
                # 看看下一个
                l += 1
                # 如果下一个墙没有当前墙高，一定会有积水在下一个墙
                left_max = max(left_max, height[l])
                count += left_max - height[l]
            # 如果左边比右边高，计算右边的积水
            else:
                # 看看下一个
                r -= 1
                # 如果下一个墙没有当前墙高，一定会有积水在下一个墙
                right_max = max(right_max, height[r])
                count += right_max - height[r]

        return count
        # time complexity O(n), space complexity O(1)
