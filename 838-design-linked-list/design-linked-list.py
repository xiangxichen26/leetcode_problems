class MyLinkedNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self._first = ListNode(0)
        self._len = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self._len:
            return -1
        cur = self._first
        for _ in range(index+1):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._len,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._len:
            return

        if index < 0 :
            index = 0  
        
        self._len += 1
        pre = self._first
        for _ in range(index):
            pre = pre.next
        
        node = MyLinkedNode(val)
        node.next = pre.next
        pre.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._len:
            return
        
        self._len -= 1
        pre = self._first

        for _ in range(index):
            pre = pre.next
        
        pre.next =  pre.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)