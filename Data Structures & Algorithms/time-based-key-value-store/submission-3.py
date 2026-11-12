class TimeMap:

    def __init__(self):
        # 使用哈希表存储数据，键为 key，值为一个列表
        # 列表中的每个元素是一个二元组 (timestamp, value)
        # 因为 set 操作的 timestamp 是严格递增的，所以每个 key 对应的列表天然按时间戳升序排列
        self.dict_head = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 将 (timestamp, value) 作为一个元组追加到对应 key 的列表末尾
        self.dict_head[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 初始化返回值为空字符串（若找不到符合条件的 timestamp，则返回空字符串）
        output = ""

        # 获取当前 key 对应的所有 (timestamp, value) 记录，若 key 不存在则返回空列表
        items = self.dict_head.get(key, [])
        
        # 初始化左右双指针，用于在有序列表中进行二分查找
        left, right = 0, len(items) - 1

        # 使用二分查找寻找小于或等于给定 timestamp 的最大时间戳
        while left <= right:
            mid = (left + right) // 2

            # 如果当前中间位置的时间戳小于或等于目标时间戳
            if items[mid][0] <= timestamp:
                # 记录当前满足条件的 value（因为是找最大的合法时间戳，后面可能有更接近目标的，所以要暂存并继续向右找）
                output = items[mid][1]
                # 收缩左边界，尝试在右半部分寻找更大的、同样满足条件的时间戳
                left = mid + 1
            # 如果当前中间位置的时间戳大于目标时间戳
            else:
                # 说明当前时间戳太大了，不符合条件，收缩右边界到左半部分查找
                right = mid - 1

        # 返回最终找到的最接近且小于等于目标时间戳的 value
        return output
        # 时间: 
        # set 操作：O(1)。仅执行了哈希表的查找和列表末尾的追加操作。
        # get 操作：O(log N)。其中 N 是当前 key 关联的记录总数。利用二分查找在有序的时间戳列表中定位结果。
        
        # 空间: O(M N)。其中 M 是不同 key 的数量，N 是每个 key 对应的平均条目数。所有的键值对及时间戳都需要存储在哈希表中。

