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
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.store = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        cur = self.store[key]

        pre_node = cur.pre
        next_node = cur.next
        pre_node.next = next_node
        next_node.pre = pre_node

        cur.next = self.tail
        cur.pre = self.tail.pre

        pre_recent_node = self.tail.pre
        self.tail.pre = cur
        pre_recent_node.next = cur

        return cur.val

    def put(self, key: int, value: int) -> None:

        if key in self.store:
            self.store[key].val = value

            cur = self.store[key]

            pre_node = cur.pre
            next_node = cur.next
            pre_node.next = next_node
            next_node.pre = pre_node

        else:
            self.store[key] = Node(key=key, val=value)

        cur = self.store[key]

        cur.next = self.tail
        cur.pre = self.tail.pre

        pre_recent_node = self.tail.pre
        self.tail.pre = cur
        pre_recent_node.next = cur

        if len(self.store) > self.capacity:
            key_remove_node = self.head.next.key
            next_node = self.head.next.next
            next_node.pre = self.head
            self.head.next = next_node

            del self.store[key_remove_node]

        return


