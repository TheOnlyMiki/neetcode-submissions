class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        record = [-1] * (len(nums) + 1)

        for num, time in count.items():
            if record[time] == -1:
                record[time] = [num]
            else:
                record[time].append(num)

        output = []
        for nums in record[::-1]:
            if nums != -1:
                output += nums
            if len(output) >= k:
                break

        return output