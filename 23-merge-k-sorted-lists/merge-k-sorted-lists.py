# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode(-1)
        p = dummy

        pq = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq,(head.val, i, head))

        while pq:
            val,i,node = heapq.heappop(pq)
            p.next = node

            if node.next:
                heapq.heappush(pq,(node.next.val, i, node.next))
            
            p = p.next
        
        return dummy.next