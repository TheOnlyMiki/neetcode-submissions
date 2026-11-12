class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []

        def backtrack(start, path):
            sums = sum(path)
            if sums == target:
                output.append(path[:])
            
            if sums < target:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i, path)
                    path.pop()

        backtrack(0, [])
        
        return output