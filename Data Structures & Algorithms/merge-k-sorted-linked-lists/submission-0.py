# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node_Compare:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head = ListNode()

        min_heap = []
        for list_node in lists:
            if list_node:
                heapq.heappush(min_heap, Node_Compare(list_node))

        if not min_heap:
            return None

        current = head

        while min_heap:
            min_node = heapq.heappop(min_heap)

            current.next = min_node.node
            current = current.next

            if min_node.node.next:
                heapq.heappush(min_heap, Node_Compare(min_node.node.next))

        return head.next