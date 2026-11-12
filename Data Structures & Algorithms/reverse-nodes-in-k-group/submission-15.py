# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        pre_head = ListNode(next=head)

        pre_group_tail = pre_head

        pre_node = None

        current = head

        count = 0

        while current:
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node

            count += 1

            if count == k:
                pre_group_head = pre_group_tail.next
                pre_group_head.next = current

                pre_group_tail.next = pre_node
                pre_group_tail = pre_group_head

                count = 0
                pre_node = None

        tail = pre_node
        pre_node = None

        while tail:
            next_node = tail.next
            tail.next = pre_node
            pre_node = tail
            tail = next_node

        pre_group_tail.next = pre_node

        return pre_head.next
