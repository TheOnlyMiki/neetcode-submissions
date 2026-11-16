class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        left, right = 0, 0

        record = defaultdict(int)

        for c in s:
            record[c] += 1

        window_count = 0
        total_count = 0
        output = []

        for c in s:
            if c in record:
                total_count += record.pop(c)

            window_count += 1
            if window_count == total_count:
                output.append(total_count)
                window_count = 0
                total_count = 0
        
        return output
