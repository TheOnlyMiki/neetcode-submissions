class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            target = -nums[i]

            left, right = i+1, len(nums)-1
            while left < right:
                sums = nums[left] + nums[right]
                if sums < target:
                    left += 1
                elif sums > target:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return output