class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Method 2 - bucket
        record = {}
        for n in nums:
            record[n] = record.get(n, 0) + 1

        count = [ [] for _ in range(len(nums)+1)] 
        for n, x in record.items():
            count[x].append(n)

        output = []
        for n in reversed(count):
            for x in n:
                output.append(x)
                if len(output) == k:
                    return output

        return output
        # time complexity O(n), space complexity O(n)
