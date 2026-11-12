class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []

        def backtrack(start, path, sums):
            if sums == target:
                output.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if sums + nums[i] > target:
                    continue
                path.append(nums[i])
                backtrack(i, path, sums + nums[i])
                path.pop()

        backtrack(0, [], 0)
        
        return output