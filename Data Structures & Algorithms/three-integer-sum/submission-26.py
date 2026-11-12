class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Method 1 - 2 sum with hash
        '''nums = sorted(nums)

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        output = []
        for i_1 in range(len(nums)-2):
            count[nums[i_1]] -= 1
            if i_1 > 0 and nums[i_1] == nums[i_1-1]:
                continue

            # two sum - hash
            for i_2 in range(i_1+1, len(nums)-1):
                count[nums[i_2]] -= 1
                if i_2 > i_1+1 and nums[i_2] == nums[i_2-1]:
                    continue

                target = -(nums[i_1] + nums[i_2])
                if count[target] > 0:
                    output.append([nums[i_1], nums[i_2], target])
            
            for i_2 in range(i_1+1, len(nums)-1):
                count[nums[i_2]] += 1

        return output'''
        # time complexity O(n^2), space complexity O(n)

        # Method 2 - 2 sum with two pointer
        nums = sorted(nums)

        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            # 2 sum two pointer
            l, r = i+1, len(nums)-1
            while l < r:
                sums = nums[l] + nums[r]
                if sums < target:
                    l += 1
                elif sums > target:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return output
