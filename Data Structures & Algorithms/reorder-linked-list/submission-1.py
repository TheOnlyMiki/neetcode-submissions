# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Method 2 - 快慢指针找中间，然后再回退

        # Method 1 - 先遍历一遍储存顺序，再倒着添加
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
        # time complexity O(n), space complexity O(n)
