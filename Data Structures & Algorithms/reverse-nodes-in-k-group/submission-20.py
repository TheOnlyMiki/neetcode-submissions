# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        pre_head = ListNode()

        pre_group_head = head

        pre_group_tail = pre_head

        cur = head
        pre_node = None

        count = 0

        while cur:
            next_node = cur.next
            cur.next = pre_node
            pre_node = cur
            cur = next_node

            count += 1

            if count == k:
                pre_group_tail.next = pre_node

                pre_group_tail = pre_group_head

                pre_group_head = cur

                pre_node = None
                count = 0

        if count == 0:
            return pre_head.next

        tail = pre_node
        pre_node = None

        while tail:
            next_node = tail.next
            tail.next = pre_node
            pre_node = tail
            tail = next_node

        pre_group_tail.next = pre_node

        return pre_head.next


































