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

        if not head:
            return head

        record = {}

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
