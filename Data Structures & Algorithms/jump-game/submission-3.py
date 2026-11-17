class Solution:
    def canJump(self, nums: List[int]) -> bool:

        most_far = 0

        for i in range(len(nums)-1):
            if i > most_far:
                return False

            most_far = max(most_far, i + nums[i])

        return True if most_far >= len(nums)-1 else False





































        
        most_far = 0

        for i in range(len(nums)-1):
            if i > most_far:
                break

            most_far = max(most_far, i + nums[i])

        return True if most_far >= len(nums)-1 else False