# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        first = head
        second = head.next

        while second and second.next:
            if first == second:
                return True

            first = first.next
            second = second.next.next

        return False