class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(l, r):
            pivot_val = nums[r]

            store = l
            for i in range(l, r):
                if nums[i] > pivot_val:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1

            nums[store], nums[r] = nums[r], nums[store]

            if store > k - 1:
                return quickSelect(l, store - 1)
            elif store < k - 1:
                return quickSelect(store + 1, r)
            else:
                return nums[store]

        return quickSelect(0, len(nums)-1)