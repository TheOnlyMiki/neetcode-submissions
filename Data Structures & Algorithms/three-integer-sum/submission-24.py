class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Method 1 - 2 sum with hash
        nums = sorted(nums)

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

        return output
