# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        
        pre, cur, nxt = None, head, head.next
        while n > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next
            n -= 1
        
        head.next = cur
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        a = b = head
        for _ in range(k):
            if not b:
                return head
            b= b.next
        
        newHead = self.reverseN(a, k)
        # 此时 b 指向下一组待反转的头结点
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k) 

        return newHead