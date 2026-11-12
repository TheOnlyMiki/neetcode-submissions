class KthLargest:
    """
    题目：设计一个类，在数据流中实时返回第 k 大的元素。
         __init__ 给出初始数组，之后每次 add 一个新数，返回当前所有数中第 k 大的值。
    思路：维护一个大小为 k 的最小堆，只保留"目前最大的 k 个数"：
         - 堆顶是这 k 个数里最小的，也就是全体数据中第 k 大的
         - 新数比堆顶小 → 它连前 k 大都进不了，直接丢弃
         - 新数比堆顶大 → 它挤进前 k 大，把原来的堆顶（第 k 大）挤出去
    时间复杂度：__init__ O(n log k)，add O(log k)
    空间复杂度 O(k)：堆中最多 k 个元素

    小提示：
    - 原代码的条件写反了：self.k < len(self.min_heap) 应为 len(self.min_heap) < self.k。
      写反后第一次 add 时堆为空，条件为 False，进入 elif 访问 self.min_heap[0]，
      会抛出 IndexError。已在下面修正。
    - 为什么用最小堆而不是最大堆：要找"第 k 大"，需要快速拿到前 k 大里最小的那个
      并能把它踢掉，这正是最小堆堆顶的作用。反过来，找"第 k 小"就用大小为 k 的最大堆。
    - heappushpop(heap, val)：先 push 再 pop，一次 O(log k)，比分开调用快。
      这里 val 一定大于堆顶，所以也可以用 heapreplace（先 pop 再 push），结果一样。
    - val == 堆顶时走不进 elif，直接丢弃也没问题：替换进去堆的内容完全不变。
    - __init__ 末尾的 return 可以省略。
    - 也可以在 __init__ 里先 heapify(nums)，再 pop 到只剩 k 个，建堆部分是 O(n)：
          self.min_heap = nums
          heapq.heapify(self.min_heap)
          while len(self.min_heap) > k:
              heapq.heappop(self.min_heap)
    - 同类题：LeetCode 215（数组中第 K 个最大元素）用的是同一个"大小为 k 的最小堆"技巧。
    """

    def __init__(self, k: int, nums: List[int]):

        self.min_heap = []   # 保存当前最大的 k 个数，堆顶为第 k 大
        self.k = k

        # 复用 add 的逻辑，逐个加入初始数据
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # ---------- 情况 1：堆还没满 k 个，直接加入 ----------
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)

        # ---------- 情况 2：堆已满，新数比堆顶大 → 替换掉堆顶 ----------
        # 新数进入前 k 大，原来的第 k 大被挤出
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)

        # 情况 3：堆已满且新数 <= 堆顶 → 进不了前 k 大，什么都不做

        # 堆顶就是当前第 k 大
        # （题目保证调用 add 返回结果时，数据至少有 k 个）
        return self.min_heap[0]