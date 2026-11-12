# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 短写法
        carry = 0

        pre_head = ListNode()
        current = pre_head

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sums = l1_val + l2_val + carry

            carry = sums // 10
            sums = sums % 10

            current.next = ListNode(val=sums)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return pre_head.next


        # 长写法
        carry = 0

        pre_head = ListNode()
        current = pre_head

        while l1 and l2:
            sums = l1.val + l2.val + carry

            if sums > 9:
                carry = 1
                current.next = ListNode(val=sums-10)
            else:
                carry = 0
                current.next = ListNode(val=sums)
            
            l1 = l1.next
            l2 = l2.next
            current = current.next

        while l1:
            sums = l1.val + carry

            if sums > 9:
                carry = 1
                current.next = ListNode(val=sums-10)
            else:
                carry = 0
                current.next = ListNode(val=sums)
            
            l1 = l1.next
            current = current.next

        while l2:
            sums = l2.val + carry

            if sums > 9:
                carry = 1
                current.next = ListNode(val=sums-10)
            else:
                carry = 0
                current.next = ListNode(val=sums)
            
            l2 = l2.next
            current = current.next

        if carry == 1:
            current.next = ListNode(val=1)

        return pre_head.next