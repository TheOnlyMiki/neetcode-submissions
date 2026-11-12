# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        题目：两个非负整数以逆序链表存储（个位在表头），求两数之和，同样以逆序链表返回。
        例：2→4→3 (342) + 5→6→4 (465) = 7→0→8 (807)
        因为是逆序存储，从表头开始相加正好是从个位开始，和竖式加法顺序一致。
        """

        # ==================== 短写法 - 统一循环 ====================
        # 时间复杂度 O(max(m, n))，空间复杂度 O(1)（不算结果链表）

        carry = 0   # 进位，只可能是 0 或 1

        # 虚拟头节点：不用特判"结果链表的第一个节点"，最后返回 pre_head.next
        pre_head = ListNode()
        current = pre_head   # current 指向结果链表的最后一个节点，用来往后接新节点

        # 只要还有一条链表没走完，或者还有进位没处理，就继续
        # 把 carry 放进条件里，就不用在循环后单独处理最高位进位（如 5 + 5 = 10）
        while l1 or l2 or carry:
            # 某条链表已走完时，当作该位为 0，相当于短的数高位补零
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # 当前位之和 = 两个数位 + 上一位的进位
            sums = l1_val + l2_val + carry

            carry = sums // 10   # 新的进位（十位）
            sums = sums % 10     # 当前位保留的数字（个位）

            # 把当前位接到结果链表末尾
            current.next = ListNode(val=sums)

            # 各指针前进；已经走完的链表保持 None
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return pre_head.next


        # ==================== 长写法 - 分三段处理 ====================
        # 注意：上面已经 return，这段代码不会执行，仅作对照保留
        # 时间复杂度 O(max(m, n))，空间复杂度 O(1)（不算结果链表）

        carry = 0

        pre_head = ListNode()
        current = pre_head

        # ---------- 第 1 段：两条链表都还有节点 ----------
        while l1 and l2:
            sums = l1.val + l2.val + carry

            # 两个一位数加进位最大为 9 + 9 + 1 = 19，所以进位最多为 1
            if sums > 9:
                carry = 1
                current.next = ListNode(val=sums-10)
            else:
                carry = 0
                current.next = ListNode(val=sums)

            l1 = l1.next
            l2 = l2.next
            current = current.next

        # ---------- 第 2 段：只剩 l1 有节点 ----------
        # 进位可能会一路传递下去（如 999 + 1），所以不能直接把 l1 剩余部分接上
        while l1:
            sums = l1.val + carry

            if sums > 9:
                carry = 1
                current.next = ListNode(val=sums-10)
            else:
                carry = 0
                current.next = ListNode(val=sums)

            l1 = l1.next
            current = current.next

        # ---------- 第 3 段：只剩 l2 有节点 ----------
        # 第 2、3 段最多只会执行其中一段
        while l2:
            sums = l2.val + carry

            if sums > 9:
                carry = 1
                current.next = ListNode(val=sums-10)
            else:
                carry = 0
                current.next = ListNode(val=sums)

            l2 = l2.next
            current = current.next

        # ---------- 第 4 步：处理最高位的进位 ----------
        # 例：5 + 5 = 10，两条链表都走完了但还有进位，需要补一个节点 1
        if carry == 1:
            current.next = ListNode(val=1)

        return pre_head.next