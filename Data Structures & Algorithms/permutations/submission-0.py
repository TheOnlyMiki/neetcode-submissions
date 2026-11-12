class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        length = len(nums)

        def backtrack(path, visit):
            if len(path) == length:
                output.append(path[:])
                return

            for i in range(length):
                if visit[i] is False:
                    visit[i] = True
                    path.append(nums[i])

                    backtrack(path, visit)

                    path.pop()
                    visit[i] = False
        
        backtrack([], [False] * length)

        return output