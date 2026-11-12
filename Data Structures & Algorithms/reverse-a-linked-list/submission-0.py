# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None
        current = head

        while current:
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node

        return pre_node