# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pre_head = ListNode()

        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                min_heap.append((lists[i].val, i, lists[i]))

        heapq.heapify(min_heap)

        cur = pre_head

        while min_heap:
            value, i, node = heapq.heappop(min_heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return pre_head.next

