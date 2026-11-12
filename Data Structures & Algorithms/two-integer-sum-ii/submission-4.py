class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            sums = numbers[l] + numbers[r]
            
            if sums < target:
                l += 1
            elif sums > target:
                r -= 1
            else:
                break

        return [l+1, r+1]
        # time complexity O(n), space complexity O(1)