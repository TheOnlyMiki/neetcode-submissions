"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        """
        题目：深拷贝一个带 random 指针的链表。
        难点：复制某个节点时，它的 random 指向的节点可能还没被复制，
             所以需要一种办法建立"原节点 → 新节点"的对应关系。
        """

        # ==================== Method 3 - 原地交织（空间 O(1)） ====================
        # 时间复杂度 O(n)，额外空间 O(1)（不算输出的新链表）
        # 思路：把每个新节点插在对应原节点后面，用"原节点.next"代替哈希表来找到它的拷贝

        if head is None:
            return None

        # ---------- 第 1 步：在每个原节点后面插入它的拷贝 ----------
        # A → B → C  变成  A → A' → B → B' → C → C'
        current = head

        while current:
            copy = Node(current.val)      # 创建拷贝节点
            copy.next = current.next      # A' → B
            current.next = copy           # A → A'
            current = copy.next           # 跳到下一个原节点 B

        # 新链表的头就是原头节点后面的那个拷贝
        new_head = head.next

        # ---------- 第 2 步：设置拷贝节点的 random ----------
        # 关键：原节点 X 的拷贝就是 X.next
        # 所以 A.random = C  ⇒  A'.random = C.next = C'
        current = head

        while current:
            if current.random:
                current.next.random = current.random.next
            # random 为 None 时，拷贝的 random 默认就是 None，不用处理

            current = current.next.next   # 跳过拷贝节点，到下一个原节点

        # ---------- 第 3 步：拆分两条链表 ----------
        # A → A' → B → B' → C → C'
        # 拆成 A → B → C（恢复原链表）和 A' → B' → C'（新链表）
        current = head

        while current:
            copy = current.next
            current.next = copy.next      # 原节点跳过拷贝，指回下一个原节点
            if copy.next:
                copy.next = copy.next.next   # 拷贝节点指向下一个拷贝节点
            # copy.next 为 None 说明已到末尾，copy.next 保持 None 即可

            current = current.next        # 前进到下一个原节点

        return new_head

        # ==================== Method 2 - defaultdict 一次遍历 ====================
        # 注意：上面已经 return，这段代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # 思路：用 defaultdict 在"第一次访问到某个原节点"时自动创建它的拷贝，
        #      这样即使 random 指向还没遍历到的节点，也能直接拿到对应拷贝

        # 访问不存在的 key 时，自动创建一个 Node(0) 作为占位拷贝
        record = defaultdict(lambda: Node(0))
        # None 必须单独映射为 None，否则访问 record[None] 会生成一个多余的节点
        record[None] = None

        current = head

        while current:
            # record[current] 可能之前已经因为被别人的 next/random 引用而创建过，
            # 这里补上真正的值
            record[current].val = current.val
            # next 和 random 指向的拷贝不存在时会被自动创建
            record[current].next = record[current.next]
            record[current].random = record[current.random]
            current = current.next

        return record[head]

        # ==================== Method 1 - 哈希表两次遍历 ====================
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # 思路：第一遍只建节点，第二遍再连指针，逻辑最直观

        # 预先放入 None → None，处理 next/random 为空的情况
        record = {None: None}

        # ---------- 第 1 步：为每个原节点创建拷贝，建立映射 ----------
        current = head

        while current:
            record[current] = Node(x=current.val)
            current = current.next

        # ---------- 第 2 步：根据映射连接 next 和 random ----------
        # 此时所有拷贝都已存在，直接查表即可
        current = head

        while current:
            record[current].next = record[current.next] if current.next else None
            record[current].random = record[current.random] if current.random else None
            current = current.next

        return record[head]