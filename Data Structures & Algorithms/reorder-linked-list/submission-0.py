# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Method 1 - 先遍历一遍倒着添加
        if not head:
            return

        current = head
        
        record = []
        
        while current:
            record.append(current)
            current = current.next

        left, right = 0, len(record)-1

        while left < right:
            record[left].next = record[right]
            left += 1

            if left >= right:
                break

            record[right].next = record[left]
            right -= 1

        record[left].next = None

        return None

