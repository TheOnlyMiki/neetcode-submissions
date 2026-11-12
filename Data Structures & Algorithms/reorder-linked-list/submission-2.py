# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Method 2 - 快慢指针找中间，然后再回退
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = None
        pre_node = None 

        while current:
            temp = current.next
            current.next = pre_node
            pre_node = current
            current = temp

        list1 = head
        list2 = pre_node

        while list2:
            list1_next = list1.next
            list2_next = list2.next

            list1.next = list2
            list2.next = list1_next

            list1 = list1_next
            list2 = list2_next

        return

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

        return 
        # time complexity O(n), space complexity O(n)
