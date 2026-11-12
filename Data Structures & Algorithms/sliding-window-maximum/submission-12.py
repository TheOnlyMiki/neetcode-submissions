class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()

        output = []

        for i in range(k-1):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)

        for i in range(k-1, len(nums)):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            window.append(i)

            if window[0] <= i-k:
                window.popleft()

            output.append(nums[window[0]])

        return output
