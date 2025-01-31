# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthEnd(self, head, n) ->  Optional[ListNode]:
        if not head:
            return None
        
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0 :
            return head
        
        p = head
        l = 0
        last = head
        while p:
            l += 1
            p = p.next
        
        n = k % l
        
        if n==0:
            return head
        
        # 获取倒数N-1个结点
        a = self.findNthEnd(head, n+1)
        
        # 获取倒数N个结点
        new_head = self.findNthEnd(head, n)

        # 获取最后一个结点
        last = self.findNthEnd(head, 1)

        last.next = head
        head = new_head
        a.next = None

        return head




        