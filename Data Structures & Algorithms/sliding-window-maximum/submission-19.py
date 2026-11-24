class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        window = deque()

        output = []

        for i in range(len(nums)):
            if window and window[0] <= i-k:
                window.popleft()

            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            window.append(i)

            output.append(nums[window[0]])

        return output[k-1:]
        
        window = deque()

        for i in range(k-1):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            window.append(i)

        output = []

        for r in range(k-1, len(nums)):

            while window and nums[window[-1]] <= nums[r]:
                window.pop()

            window.append(r)

            if window[0] <= r-k:
                window.popleft()

            output.append(nums[window[0]])

        return output
