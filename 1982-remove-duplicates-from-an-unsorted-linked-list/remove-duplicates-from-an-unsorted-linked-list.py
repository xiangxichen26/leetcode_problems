# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # Edge Case:
        if not head:
            return None

        visit = {}
        # traverse the linked list and calculate the frequency of each val
        p = head
        while p:
             visit[p.val] = visit.get(p.val,0) + 1
             p = p.next
        
        dummy_uniqe = ListNode(-1)
        p_uniqe = dummy_uniqe
        p = head
        while p:
            # find unique val
            if visit[p.val] == 1:
                p_uniqe.next = p
                p_uniqe = p_uniqe.next
            # delete the node
            temp = p.next
            p.next = None
            p = temp
        
        return dummy_uniqe.next


