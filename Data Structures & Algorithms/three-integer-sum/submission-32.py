class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        nums.sort()

        output = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            l, r = i+1, n-1

            while l < r:
                sums = nums[l] + nums[r]
                
                if sums > target:
                    r -= 1
                elif sums < target:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return output

        















































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