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

        # Method 2 - 遍历一遍储存进预先设置好的hash
        record = defaultdict(lambda:Node(0))
        record[None] = None

        current = head

        while current:
            record[current].val = current.val
            record[current].next = record[current.next]
            record[current].random = record[current.random]
            current = current.next

        return record[head]

        # Method 1 - 先遍历一遍储存进hash，然后一一配对

        record = {None:None}

        current = head

        while current:
            record[current] = Node(x=current.val)
            current = current.next

        current = head

        while current:
            record[current].next = record[current.next] if current.next else None
            record[current].random = record[current.random] if current.random else None
            current = current.next

        return record[head]
