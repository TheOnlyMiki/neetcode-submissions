class TimeMap:

    def __init__(self):
        self.dict_head = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_head[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        output = ""

        items = self.dict_head.get(key, [])
        left, right = 0, len(items) - 1

        while left <= right:
            mid = (left + right) // 2

            if items[mid][0] <= timestamp:
                left = mid + 1
                output = items[mid][1]
            else:
                right = mid - 1

        return output
