class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        nums = sorted(nums)

        length = len(nums)

        def backtrack(start, path):
            output.append(path[:])

            for i in range(start, length):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])

                backtrack(i+1, path)

                path.pop()

        backtrack(0, [])

        return output