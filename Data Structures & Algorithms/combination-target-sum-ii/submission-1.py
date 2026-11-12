class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        output = []

        candidates = sorted(candidates)
        
        def backtrack(start, path, sums):
            if sums == target:
                output.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if sums + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, path, sums + candidates[i])
                path.pop()

        backtrack(0, [], 0)

        return output