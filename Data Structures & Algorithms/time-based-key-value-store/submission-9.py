class TimeMap:

    def __init__(self):
        self.record = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.record[key].append((timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        
        if len(self.record[key]) == 0:
            return ""

        array = self.record[key]

        l, r = 0, len(array)-1

        output = ""

        while l <= r:
            mid = (l+r)//2

            if array[mid][0] <= timestamp:
                output = array[mid][1]
                l = mid +1
            else:
                r = mid -1

        return output