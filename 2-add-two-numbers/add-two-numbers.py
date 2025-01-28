# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        # 虚拟头结点（构建新链表时的常用技巧）
        dummy = ListNode(-1)
        # 指针 p 负责构建新链表
        p = dummy
        # 记录进位
        carry = 0

        while p1 is not None or p2 is not None or carry > 0:
            # 先加上上次的进位
            val = carry
            if p1 is not None:
                val += p1.val
                p1 = p1.next
            if p2 is not None:
                val += p2.val
                p2 = p2.next
            # 处理进位情况
            carry = val // 10
            val = val % 10
            # 构建新节点
            p.next = ListNode(val)
            p = p.next
        # 返回结果链表的头结点（去除虚拟头结点）
        return dummy.next
        

        
            
            

        