class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        record = defaultdict(int)

        for num in nums:
            record[num] += 1

        bucket = [[] for i in range(len(nums)+1)]

        for num, count in record.items():
            bucket[count].append(num)

        output = []

        for i in range(len(nums), -1, -1):
            if len(bucket[i]) == 0:
                continue

            for num in bucket[i]:
                output.append(num)
                if len(output) == k:
                    return output

        return output







































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

        '''count = [ [] for _ in range(len(nums)+1)] 
        for n, x in record.items():
            count[x].append(n)

        output = []
        for n in reversed(count):
            for x in n:
                output.append(x)
                if len(output) == k:
                    break'''

        count = [0] * (len(nums) + 1)
        for n, x in record.items():
            if count[x] == 0:
                count[x] = [n]
            else:
                count[x].append(n)

        output = []
        for n in count[::-1]:
            if n != 0:
                output += n
            if len(output) >= k:
                break

        return output
        # time complexity O(n), space complexity O(n)
