class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            cur = nums[mid]

            if nums[left] < nums[right]:
                return nums[left]
            elif cur > nums[right]:
                left = mid + 1
            else:
                right = mid


        return nums[left]