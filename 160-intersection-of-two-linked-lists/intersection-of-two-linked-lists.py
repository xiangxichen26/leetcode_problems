# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_length(self, head: ListNode) -> int:
        count = 0
        cur = head

        while cur:
            count += 1 
            cur = cur.next
        
        return count

    def move_start_pointer(self, head: ListNode, step:int) -> Optional[ListNode]:
        cur = head
        for _ in range(step):
            cur = cur.next
        
        return cur
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        diff = self.get_length(headA) - self.get_length(headB)

        if diff > 0:
            curA = self.move_start_pointer(headA, diff)
            curB = headB
        elif diff == 0:
            curA = headA
            curB = headB
        else:
            curA = headA
            curB = self.move_start_pointer(headB, -diff)
        
        while curA and curB:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        
        return None