class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:

        if self.left_max and num < -self.left_max[0]:
            heapq.heappush(self.left_max, -num)
        else:
            heapq.heappush(self.right_min, num)

        if len(self.left_max) > len(self.right_min) + 1:
            num = heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, -num)
        elif len(self.right_min) > len(self.left_max) + 1:
            num = heapq.heappop(self.right_min)
            heapq.heappush(self.right_min, -num)

    def findMedian(self) -> float:
        if len(self.left_max) > len(self.right_min):
            return self.left_max[0]
        elif len(self.left_max) < len(self.right_min):
            return self.right_min[0]
        else:
            return (self.left_max[0] + self.right_min[0]) / 2.0
















    """
    题目：数据流的中位数。不断加入数字，随时返回当前所有数字的中位数。
    思路：对顶堆（两个堆），把所有数分成"较小的一半"和"较大的一半"：
    - left_max：较小的一半，用最大堆（存负数），堆顶是较小一半中最大的数
    - right_min：较大的一半，用最小堆，堆顶是较大一半中最小的数
    维护两个不变量：
    1. 有序：left_max 中所有数 <= right_min 中所有数
    2. 平衡：两个堆的大小相差不超过 1
    这样中位数只和两个堆顶有关：
    - 总数为奇数 → 中位数是元素较多那个堆的堆顶
    - 总数为偶数 → 中位数是两个堆顶的平均值
    例：依次加入 5, 2, 8, 3
        left_max = [3, 2]（最大 3），right_min = [5, 8]（最小 5）
        中位数 = (3 + 5) / 2 = 4.0
    复杂度：addNum O(log n)，findMedian O(1)，空间 O(n)

    小提示：
    - left_max 为空时新数一律放进 right_min，看起来可能把小数放错边，但不会出错：
      left_max 为空时 right_min 最多只有 1 个元素，放入后若变成 2 个，
      平衡步骤会把其中较小的那个移到 left_max，有序性依然成立。
    - 两个平衡判断最多只有一个会触发（每次只加入一个数，大小差最多变化 1）。
    - 更常见的约定是固定让 left_max 的大小等于 right_min 或多 1，
      这样 findMedian 只需判断奇偶：奇数返回 -left_max[0]，偶数取平均，少一个分支。
      对应的 addNum 常写成"先放进 left，再把 left 的最大值挪到 right，最后若 right 更大再挪回来"，
      每次固定 3 次堆操作，不需要比较 num 与堆顶。
    - 面试常见追问：
      · 如果所有数都在 [0, 100]：用长度 101 的计数数组，找中位数时累加计数，O(100) = O(1)
      · 如果 99% 的数在 [0, 100]：计数数组 + 两个列表分别存 < 0 和 > 100 的数，
        中位数几乎一定落在计数数组里
      · 滑动窗口中位数（LeetCode 480）：对顶堆 + 延迟删除，难度更高
    """

    def __init__(self):

        # 较大的一半，最小堆，堆顶为较大一半中的最小值
        self.right_min = []
        # 较小的一半，最大堆（存负数），堆顶取负为较小一半中的最大值
        self.left_max = []

    def addNum(self, num: int) -> None:

        # ---------- 第 1 步：按大小放进对应的堆，保持有序性 ----------
        # 比较小一半的最大值还小 → 属于较小的一半
        if self.left_max and num < -self.left_max[0]:
            heapq.heappush(self.left_max, -num)
        # 否则（包括 left_max 为空）→ 放进较大的一半
        else:
            heapq.heappush(self.right_min, num)

        # ---------- 第 2 步：平衡两个堆的大小，差值不超过 1 ----------
        # left 多出 2 个：把 left 的最大值移到 right
        # （移动的是边界上的数，有序性不会被破坏）
        if len(self.left_max) > len(self.right_min) + 1:
            val = heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, -val)

        # right 多出 2 个：把 right 的最小值移到 left
        if len(self.right_min) > len(self.left_max) + 1:
            val = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -val)

    def findMedian(self) -> float:

        # 总数为奇数，left 多一个 → 中位数是 left 的最大值
        if len(self.left_max) > len(self.right_min):
            return -self.left_max[0]

        # 总数为奇数，right 多一个 → 中位数是 right 的最小值
        elif len(self.left_max) < len(self.right_min):
            return self.right_min[0]

        # 总数为偶数 → 两个堆顶的平均值
        # left_max 存的是负数，所以 right_min[0] - left_max[0] = 较大堆顶 + 较小堆顶
        else:
            return (self.right_min[0] - self.left_max[0]) / 2.0