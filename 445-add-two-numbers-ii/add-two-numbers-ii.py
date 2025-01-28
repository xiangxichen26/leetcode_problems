# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        stk1 = []
        stk2 = []
        dummy = ListNode(-1)
        
        while p1:
            stk1.append(p1.val)
            p1 = p1.next
        while p2:
            stk2.append(p2.val)
            p2 = p2.next
        
        carry = 0
        while stk1 or stk2 or carry > 0:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            
            carry = val // 10
            val = val % 10

            newNode = ListNode(val)
            newNode.next = dummy.next
            dummy.next = newNode
        
        return dummy.next


        