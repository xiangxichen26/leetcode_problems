# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKthFromEnd(self, head, k) -> Optional[ListNode]:
        if not head:
            return head
        left = head
        right = head
        
        for _ in range(k):
            right= right.next

        while right:
            left = left.next
            right = right.next
        
        return left
    
    def findKth(self, head, k) -> Optional[ListNode]:
        if not head or k == 0: 
            return head
        p = head

        for _ in range(1,k):
            p = p.next
        
        return p

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 找到倒数K个结点
        k1End = self.findKthFromEnd(head,k)

        # 找到正数K个结点
        k1Front = self.findKth(head,k)

        k1End.val, k1Front.val = k1Front.val, k1End.val

        return head



