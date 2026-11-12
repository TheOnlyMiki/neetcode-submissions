class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

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

        return count
