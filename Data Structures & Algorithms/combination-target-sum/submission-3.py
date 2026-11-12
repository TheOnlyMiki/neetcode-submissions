class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []

        def backtrack(start, path):
            sums = sum(path)
            if sums == target:
                output.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if nums[i] + sums > target:
                    continue
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, [])
        
        return output