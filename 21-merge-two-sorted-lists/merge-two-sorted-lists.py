# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(101)
        p = dummy

        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                temp = list1.next
                list1.next = None
                list1 = temp
            else:
                p.next = list2
                temp = list2.next
                list2.next = None
                list2 = temp  
            p = p.next
        
        while list1:
            p.next = list1
            p = p.next
            list1 = list1.next
        
        while list2:
            p.next = list2
            p = p.next
            list2 = list2.next
        
        p.next = None
        return dummy.next


        