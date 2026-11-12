# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        题目：每 k 个节点一组进行反转，最后不足 k 个的节点保持原顺序。
        例：1→2→3→4→5，k = 2  →  2→1→4→3→5
            1→2→3→4→5，k = 3  →  3→2→1→4→5
        """

        # ==================== Method 2 - 边反转边衔接 ====================
        # 时间复杂度 O(n)，空间复杂度 O(1)
        # 思路：一路逐个反转节点，每凑满 k 个就把这一组接到前一组后面；
        #      走到末尾后，把不足 k 个的那段再反转回来

        # 虚拟头节点：第一组反转后头节点会变，用它统一处理
        pre_head = ListNode(next=head)

        # 上一组（已处理好）的尾节点，初始为虚拟头
        # 不变量：pre_group_tail.next 始终指向"当前组反转前的第一个节点"
        pre_group_tail = pre_head

        current = head      # 当前要反转的节点
        pre_node = None     # 当前组内已反转部分的头节点
        count = 0           # 当前组已反转的节点个数

        while current:
            # ---------- 标准反转：把 current 指向 pre_node ----------
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node

            count += 1

            # ---------- 凑满 k 个：把这一组接回链表 ----------
            if count == k:
                count = 0

                # 这一组反转前的第一个节点，反转后变成了这一组的尾
                pre_group_head = pre_group_tail.next

                # 上一组的尾 → 这一组反转后的头
                pre_group_tail.next = pre_node

                # 这一组的尾成为新的"上一组尾"
                pre_group_tail = pre_group_head

                # 先让它指向下一组反转前的第一个节点，维持不变量
                # （若下一组凑满，会在下次 count == k 时被改成正确的头）
                pre_group_tail.next = current

                # 开始新的一组
                pre_node = None

        # ---------- 处理末尾不足 k 个的节点 ----------
        # 循环结束时，最后 count 个节点已经被反转了，需要再反转回原顺序
        # 例：1→2→3→4→5，k = 3，剩下 4、5 被反转成 5→4，这里恢复成 4→5
        tail = pre_node     # 被反转的剩余部分的头（若刚好整除则为 None）
        pre_node = None

        while tail:
            next_node = tail.next
            tail.next = pre_node
            pre_node = tail
            tail = next_node

        # 接到最后一个完整组的尾部（刚好整除时 pre_node 为 None，结尾正确置空）
        pre_group_tail.next = pre_node

        return pre_head.next

        # ==================== Method 1 - 先分组反转存入数组，再依次连接 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(n / k)（数组存每组的头）
        # 思路：第一遍把每 k 个反转成一段独立的小链表，存下每段的头；
        #      第二遍把各段首尾相连；最后把不足 k 个的剩余部分反转回来接上

        groups = []   # 存每个反转后小链表的头节点

        current = head
        pre_node = None
        count = 0

        # ---------- 第 1 步：逐个反转，每满 k 个切成一段 ----------
        while current:
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node

            count += 1

            if count == k:
                count = 0
                groups.append(pre_node)   # 记录这一段反转后的头
                pre_node = None           # 下一段从空开始，各段之间断开

        # 剩余不足 k 个的部分（已被反转），留到最后处理
        tail = pre_node

        # 第一段反转后的头就是最终答案的头
        # （题目保证 k <= n，至少有一组，groups[0] 不会越界）
        head = groups[0]

        n = len(groups)

        # 末尾补一个 None，让最后一段在循环里也能统一处理（groups[i + 1] 不越界）
        groups.append(None)

        # ---------- 第 2 步：把各段首尾相连 ----------
        for i in range(n):
            # 从这一段的头走到尾（每段 k 个节点，总共 O(n)）
            node = groups[i]
            while node.next:
                node = node.next

            # 这一段的尾 → 下一段的头
            node.next = groups[i + 1]

            # 把 groups[i] 改存为这一段的尾，方便后面接剩余部分
            # （下一轮循环找尾时，因为已经接上了下一段，
            #   所以必须在接之前找好尾 —— 当前写法正是先找尾再连接）
            groups[i] = node

        # 去掉补上的 None，此时 groups[-1] 是最后一个完整段的尾
        groups.pop()

        # ---------- 第 3 步：把剩余部分反转回原顺序 ----------
        # 剩余部分恰好 count 个节点（整除时 count 为 0，循环不执行）
        pre_node = None

        for _ in range(count):
            next_node = tail.next
            tail.next = pre_node
            pre_node = tail
            tail = next_node

        # 接到最后一个完整段的尾部
        groups[-1].next = pre_node

        return head