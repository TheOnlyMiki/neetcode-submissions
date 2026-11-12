class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        题目：每次取出最重的两块石头 x <= y 相撞：
             - x == y：两块都粉碎
             - x != y：x 粉碎，y 变成 y - x 放回去
             最后最多剩一块石头，返回它的重量；没有剩下则返回 0。
        思路：每次都要取"当前最大的两个" → 最大堆
             Python 的 heapq 只有最小堆，所以把重量取负存进去：
             最重的石头 → 最小的负数 → 在堆顶
        时间复杂度 O(n log n)：最多 n - 1 次碰撞，每次堆操作 O(log n)
        空间复杂度 O(n)：堆

        小提示：
        - 预先放入的 0 是一个哨兵，作用有两个：
          · 所有石头都粉碎时，堆里只剩 [0]，直接返回 0，不用单独判断空堆
          · 只剩一块真石头 s 时，堆为 [-s, 0]，循环会再执行一次：
            弹出 -s 和 0，remain = 0 - (-s) = s，放回 -s，堆变成 [-s]，长度为 1 退出
            相当于"和重量 0 的石头相撞"，结果不变，所以循环条件可以统一写成 len != 1
          哨兵 0 比所有负数都大，永远最后才会被弹出，不会干扰正常的碰撞。
        - 建堆可以用 heapify，O(n) 比逐个 push 的 O(n log n) 更快：
              max_heap = [-s for s in stones] + [0]
              heapq.heapify(max_heap)
        - 最后的 abs(max_heap[0]) 也可以写成 -max_heap[0]，堆中元素都 <= 0，两者等价。
        - Python 3.14 起 heapq 新增了 heappush_max / heappop_max 等最大堆函数，
          可以不用取负；但 LeetCode 和多数面试环境版本较旧，取负仍是最通用的写法。
        - 同类"每次取最大/最小"的堆题：LeetCode 1046（本题）、703（数据流中第 K 大元素）、
          215（数组中第 K 个最大元素）、973（最接近原点的 K 个点）。
        """

        # 最大堆（存负数），预先放入哨兵 0

        # 所有石头取负后入堆
        max_heap = [-s for s in stones] + [0]
        heapq.heapify(max_heap)

        # 堆中只剩一个元素时结束（要么是哨兵 0，要么是最后剩下的那块石头）
        while len(max_heap) != 1:
            # 依次弹出最重和第二重的石头（都是负数）
            stone_1 = heapq.heappop(max_heap)   # -y，最重
            stone_2 = heapq.heappop(max_heap)   # -x，第二重

            # 剩余重量 = y - x = (-x) - (-y) = stone_2 - stone_1，一定 >= 0
            remain = stone_2 - stone_1

            # 两块重量不同，较重的那块剩下 y - x，放回堆中（取负）
            # 重量相同时 remain 为 0，两块都粉碎，不放回
            if remain != 0:
                heapq.heappush(max_heap, -remain)

        # 堆顶为剩下的石头（取负存储），或者哨兵 0
        return abs(max_heap[0])