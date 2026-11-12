# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        题目：L0 → L1 → … → Ln-1 → Ln  重排为  L0 → Ln → L1 → Ln-1 → L2 → …
        要求原地修改，不返回值。
        """

        # ==================== Method 2 - 快慢指针 + 反转后半段 + 交替合并 ====================
        # 时间复杂度 O(n)，空间复杂度 O(1)

        # ---------- 第 1 步：快慢指针找中点 ----------
        # fast 每次走两步，slow 每次走一步；fast 到尾时 slow 正好在中间
        # 奇数长度（1→2→3→4→5）：slow 停在 3（正中间）
        # 偶数长度（1→2→3→4）  ：slow 停在 2（前半段的最后一个）
        # 这样保证前半段长度 >= 后半段长度，方便后面合并
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ---------- 第 2 步：断开链表，并反转后半段 ----------
        current = slow.next   # 后半段的起点
        slow.next = None      # 切断：前半段以 slow 结尾，避免成环
        pre_node = None       # 反转后新链表的头（初始为空）

        # 标准的迭代反转链表
        while current:
            temp = current.next       # 先保存下一个节点，防止断链后丢失
            current.next = pre_node   # 当前节点指向前一个节点（反转指针）
            pre_node = current        # pre_node 前进到当前节点
            current = temp            # current 前进到原来的下一个节点
        # 循环结束后 pre_node 是反转后后半段的头
        # 例：1→2→3→4→5  变成  前半段 1→2→3，后半段 5→4

        # ---------- 第 3 步：交替合并两段 ----------
        list1 = head       # 前半段指针
        list2 = pre_node   # 反转后的后半段指针

        # 后半段长度 <= 前半段，所以以 list2 为循环条件即可
        while list2:
            # 先保存两边的下一个节点
            list1_next = list1.next
            list2_next = list2.next

            # 把 list2 当前节点插到 list1 当前节点后面
            list1.next = list2         # L(i) → L(n-i)
            list2.next = list1_next    # L(n-i) → L(i+1)

            # 两个指针各自前进一步
            list1 = list1_next
            list2 = list2_next
        # 例：1→2→3 与 5→4 合并为 1→5→2→4→3

        return

        # ==================== Method 1 - 数组记录节点 + 双指针重连 ====================
        # 注意：上面已经 return，这段代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(n)

        # ---------- 第 1 步：遍历链表，把每个节点按顺序存进数组 ----------
        # 这样就能用下标 O(1) 访问任意位置的节点
        current = head
        record = []

        while current:
            record.append(current)
            current = current.next

        # ---------- 第 2 步：左右双指针，交替连接首尾 ----------
        left, right = 0, len(record) - 1

        while left < right:
            # 左边节点指向右边节点：L(left) → L(right)
            record[left].next = record[right]
            left += 1

            # 左右指针相遇，说明所有节点都已连好
            if left >= right:
                break

            # 右边节点指向下一个左边节点：L(right) → L(left+1)
            record[right].next = record[left]
            right -= 1

        # ---------- 第 3 步：处理尾节点 ----------
        # 循环结束时 record[left] 是重排后的最后一个节点
        # 必须把它的 next 置空，否则它仍指向原链表中的下一个节点，会形成环
        record[left].next = None

        return