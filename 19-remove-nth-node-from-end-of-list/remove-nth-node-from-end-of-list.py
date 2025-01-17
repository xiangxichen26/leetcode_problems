# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthFromEnd(self, head, k):
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        while p1 != None:
            p2 = p2.next
            p1 = p1.next
        # p2 现在指向第 n - k + 1 个节点，即倒数第 k 个节点
        return p2
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        x = self.findNthFromEnd(dummy, n+1)
        x.next = x.next.next
        
        return dummy.next



