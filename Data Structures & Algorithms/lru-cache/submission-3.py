class Node:
    """
    双向链表节点
    同时存 key 和 val：淘汰尾部节点时，需要通过 key 去哈希表里删除对应条目
    """
    def __init__(self, key=0, val=0, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache:
    """
    LRU（最近最少使用）缓存：get 和 put 都要求 O(1)
    数据结构：哈希表 + 双向链表
    - 哈希表：key → 节点，O(1) 找到节点
    - 双向链表：按使用时间排序，靠近 head 的是最近使用的，靠近 tail 的是最久未使用的
      O(1) 删除任意节点、O(1) 插到头部、O(1) 删除尾部

    链表结构：head ⇄ 最近使用 ⇄ ... ⇄ 最久未使用 ⇄ tail
    """

    def __init__(self, capacity: int):
        self.capacity = capacity   # 缓存容量

        # 虚拟头、尾节点（哨兵）：真实节点永远在两者之间，
        # 插入和删除时不用判断"前驱/后继是否为空"
        self.head = Node()
        self.tail = Node()

        # 初始为空链表：head ⇄ tail
        self.head.next = self.tail
        self.tail.pre = self.head

        # 哈希表：key → 链表节点
        # 元素个数直接用 len(self.record) 获取，不再单独维护 count
        self.record = {}

    # ==================== 辅助方法 ====================

    def _remove(self, node: Node) -> None:
        """把 node 从链表中摘下：pre ⇄ node ⇄ next  变成  pre ⇄ next"""
        node.pre.next = node.next
        node.next.pre = node.pre

    def _add_to_head(self, node: Node) -> None:
        """把 node 插到 head 后面（标记为最近使用）：head ⇄ first  变成  head ⇄ node ⇄ first"""
        # 先设置 node 自己的指针
        node.pre = self.head
        node.next = self.head.next
        # 再修改两侧邻居的指针
        # 注意顺序：必须先改 self.head.next.pre，再改 self.head.next，
        # 否则 self.head.next 已经变成 node，就找不到原来的第一个节点了
        self.head.next.pre = node
        self.head.next = node

    def _move_to_head(self, node: Node) -> None:
        """把已在链表中的 node 移到头部"""
        self._remove(node)
        self._add_to_head(node)

    # ==================== 主要接口 ====================

    def get(self, key: int) -> int:
        # key 不存在，按题意返回 -1
        if key not in self.record:
            return -1

        node = self.record[key]
        self._move_to_head(node)   # 访问过 → 变成最近使用
        return node.val

    def put(self, key: int, value: int) -> None:
        # ---------- 情况 1：key 已存在 → 更新值并移到头部 ----------
        if key in self.record:
            node = self.record[key]
            node.val = value
            self._move_to_head(node)
            return   # 元素个数不变，不需要淘汰

        # ---------- 情况 2：key 不存在 → 新建节点插到头部 ----------
        node = Node(key=key, val=value)
        self._add_to_head(node)
        self.record[key] = node

        # ---------- 超出容量：淘汰最久未使用的节点（tail 前面那个） ----------
        if len(self.record) > self.capacity:
            drop_node = self.tail.pre
            self._remove(drop_node)
            del self.record[drop_node.key]   # 这就是 Node 里要存 key 的原因