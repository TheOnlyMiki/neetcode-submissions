# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Method 1 - 先倒过来记住每个K-group在数组，然后按顺序叠回去
        
        groups = []

        current = head

        pre_node = None

        count = 0

        while current:
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node

            count += 1

            if count == k:
                count = 0
                groups.append(pre_node)
                pre_node = None

        tail = pre_node
        head = groups[0]

        n = len(groups)

        groups.append(None)

        for i in range(n):
            node = groups[i]
            while node.next:
                node = node.next

            node.next = groups[i+1]
            groups[i] = node

        groups.pop()

        pre_node = None

        for _ in range(count):
            next_node = tail.next
            tail.next = pre_node
            pre_node = tail
            tail = next_node

        groups[-1].next = pre_node

        return head

