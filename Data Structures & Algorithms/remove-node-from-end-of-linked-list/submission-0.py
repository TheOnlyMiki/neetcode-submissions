# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Method 1 - 遍历一遍储存,然后删除

        current = head

        record = []

        while current:
            record.append(current)
            current = current.next

        i = len(record) - n

        if i == 0:
            return head.next
        else:
            record[i-1].next = record[i].next

        return head
