# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reserveList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
            
        pre = None
        cur = head
        nxt = head.next

        while cur:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle node, use two pointer
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # if fast != None, which means it has odd nodes, so slow = slow.next
        if fast:
            slow = slow.next
        
        # reserve the half list
        left = head
        right = self.reserveList(slow)

        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True
        


        
     
        