# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyUni = ListNode(101)
        dummyDup = ListNode(101)

        p1 = dummyUni 
        p2 = dummyDup
        p = head

        while p:
            if (p.next is not None and p.val == p.next.val) or p.val == p2.val:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
        
            p = p.next
            p1.next = None
            p2.next = None

        return dummyUni.next
                

