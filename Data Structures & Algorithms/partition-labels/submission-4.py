class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        record_last_index = {}
        for i, c in enumerate(s):
            record_last_index[c] = i

        output = []
        last_index = 0
        count = 0

        for i, c in enumerate(s):
            count += 1
            last_index = max(last_index, record_last_index[c])

            if i == last_index:
                output.append(count)
                count = 0

        return output

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
