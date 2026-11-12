# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pre_head = ListNode(next=head)
        record_head = pre_head

        current = head

        for _ in range(n):
            current = current.next

        while current:
            pre_head = pre_head.next
            current = current.next

        pre_head.next = pre_head.next.next

        return record_head.next






























        """
        题目：删除链表的倒数第 n 个节点，返回新的头节点。
        """

        # ==================== Method 2 - 双指针（一次遍历） ====================
        # 时间复杂度 O(n)，空间复杂度 O(1)

        # ---------- 第 1 步：创建虚拟头节点 ----------
        # pre_head → head → ...
        # 作用：当要删除的恰好是头节点时（n == 链表长度），
        # 也能用统一的 "left.next = left.next.next" 处理，不用特判
        pre_head = ListNode(next=head)

        # left 从虚拟头出发，right 从真实头出发
        # 两者起点相差一步，这样最后 left 会停在"待删节点的前一个"
        left, right = pre_head, head

        # ---------- 第 2 步：right 先走 n 步 ----------
        # 走完后 left 与 right 之间间隔 n 个节点
        for _ in range(n):
            right = right.next

        # ---------- 第 3 步：两指针同步前进，直到 right 走出链表 ----------
        # right 为 None 时，left 正好在倒数第 n 个节点的前一个位置
        # 例：1→2→3→4→5，n=2
        #     right 先走到 3；同步走后 right=None，left 停在 3
        #     left.next = 4 就是倒数第 2 个
        while right:
            left = left.next
            right = right.next

        # ---------- 第 4 步：跳过待删节点 ----------
        left.next = left.next.next

        # 返回虚拟头的下一个（头节点可能已被删除，所以不能直接返回 head）
        return pre_head.next

        # ==================== Method 1 - 数组记录节点后删除 ====================
        # 注意：上面已经 return，这段代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(n)

        # ---------- 第 1 步：遍历链表，按顺序存下所有节点 ----------
        current = head
        record = []

        while current:
            record.append(current)
            current = current.next

        # ---------- 第 2 步：计算待删节点的正向下标 ----------
        # 倒数第 n 个 = 正数下标 len - n
        i = len(record) - n

        # ---------- 第 3 步：删除 ----------
        if i == 0:
            # 删除的是头节点，没有前驱，直接返回第二个节点
            return head.next
        else:
            # 让前驱节点跳过待删节点
            record[i-1].next = record[i].next

        return head