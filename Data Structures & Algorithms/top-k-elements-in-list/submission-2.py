class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1 - dict + sorted
        '''
        record = {}
        for n in nums:
            record[n] = record.get(n, 0) + 1

        count = []
        for n, x in record.items():
            count.append([x, n])

        count = sorted(count, reverse=True)

        return [ count[i][1] for i in range(k) ]'''
        # time complexity O(nlogn), space complexity O(n)

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

        return output[:k]
