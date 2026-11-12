class Node:
    def __init__(self, key=0, val=0, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.pre = self.head

        self.record = defaultdict(lambda:Node())

    def get(self, key: int) -> int:
        if key not in self.record:
            return - 1

        current = self.record[key]

        current_pre = current.pre
        current_next = current.next

        current_pre.next = current_next
        current_next.pre = current_pre

        pre_first = self.head.next

        self.head.next = current
        pre_first.pre = current

        current.next = pre_first
        current.pre = self.head

        return current.val

    def put(self, key: int, value: int) -> None:

        if key in self.record:
            current = self.record[key]
            current.val = value

            current_pre = current.pre
            current_next = current.next

            current_pre.next = current_next
            current_next.pre = current_pre

            pre_first = self.head.next

            self.head.next = current
            pre_first.pre = current

            current.next = pre_first
            current.pre = self.head

            return

        current = Node(
            key = key,
            val = value,
            next = self.head.next,
            pre = self.head
        )

        pre_first = self.head.next
            
        self.head.next = current
        pre_first.pre = current

        self.record[key] = current

        self.count += 1

        if self.count > self.capacity:
            drop_node = self.tail.pre

            drop_node.pre.next = self.tail
            self.tail.pre = drop_node.pre

            del self.record[drop_node.key]
            del drop_node
            
