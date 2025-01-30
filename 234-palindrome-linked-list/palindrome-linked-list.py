# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk = []

        p = head
        
        while p:
            stk.append(p.val)
            p = p.next
        
        while stk:
            if stk.pop() == head.val:
                head= head.next
            else:
                return False
        return True

        
     
        