# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        辅助方法：合并两个升序链表（即 LeetCode 21），供 Method 2 使用
        时间复杂度 O(m + n)，空间复杂度 O(1)
        """
        pre_head = ListNode()   # 虚拟头节点
        current = pre_head

        # 两条链表都还有节点时，每次取较小的接到结果后面
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # 最多只有一条链表有剩余，且剩余部分本身有序，直接整段接上
        current.next = l1 if l1 else l2

        return pre_head.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        题目：合并 k 个升序链表为一个升序链表。
        """

        # ==================== Method 2 - 分治（两两合并，迭代写法） ====================
        # 时间复杂度 O(N log k)：共合并 log k 轮，每轮所有节点各被访问一次
        # 空间复杂度 O(1)：迭代实现，没有递归栈，也不需要堆
        # 思路：像归并排序一样，每轮把相距 interval 的两条链表合并，
        #      interval 每轮翻倍，最终所有链表都合并进 lists[0]
        # 例：k = 5，lists = [L0, L1, L2, L3, L4]
        #     interval = 1：L0+L1 → lists[0]，L2+L3 → lists[2]，L4 不动
        #     interval = 2：lists[0]+lists[2] → lists[0]，lists[4] 不动
        #     interval = 4：lists[0]+lists[4] → lists[0]
        #     interval = 8 >= 5，结束

        if not lists:
            return None

        n = len(lists)
        interval = 1   # 当前轮要合并的两条链表在数组中的间距

        while interval < n:
            # i 每次跳 2 * interval，合并 lists[i] 和 lists[i + interval]
            # range 上界取 n - interval，保证 i + interval 不越界
            # 落单的那条链表这一轮不动，留到下一轮再合并
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

        # ==================== Method 1 - 最小堆 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(N log k)：N 为节点总数，每个节点进出堆一次，堆大小最多 k
        # 空间复杂度 O(k)：堆中最多 k 个元素（结果链表复用原节点，不额外占空间）
        # 思路：堆里始终只放每条链表"当前还没合并的第一个节点"，
        #      每次弹出最小的接到结果后面，再把它的下一个节点放进堆
        #
        # 堆中元素为元组 (节点值, 链表编号, 节点)：
        # - heapq 按元组逐项比较，先比节点值
        # - 节点值相同时比较链表编号 i，而 i 各不相同，所以永远不会比较到第三项
        # - 这样就不需要给 ListNode 定义 __lt__（ListNode 之间无法直接比较，会报 TypeError）

        # 虚拟头节点，最后返回 head.next
        head = ListNode()

        # ---------- 第 1 步：把每条链表的头节点放进最小堆 ----------
        min_heap = []
        for i, node in enumerate(lists):
            if node:   # 跳过空链表
                heapq.heappush(min_heap, (node.val, i, node))

        # 堆为空时 while 不执行，head.next 为 None，自动处理了全空的情况

        current = head   # 指向结果链表的最后一个节点

        # ---------- 第 2 步：不断弹出最小节点，接到结果链表后面 ----------
        while min_heap:
            # 堆顶就是当前所有候选节点中值最小的
            _, i, node = heapq.heappop(min_heap)

            # 直接复用原节点，接到结果末尾
            current.next = node
            current = current.next

            # 这个节点所在链表还有后续节点，就把下一个节点补进堆
            # 沿用同一个编号 i，保证堆里始终有每条未合并完的链表的"排头兵"
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return head.next
