class MyLinkedNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self._first = None
        self._len = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self._len:
            return -1
        
        cur = self._first
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._len,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._len:
            return

        self._len += 1
        new_node = MyLinkedNode(val)
        # Insert at head
        if index <= 0:
            new_node.next = self._first
            self._first = new_node
        
        else:
            pre = self._first
            for _ in range(index-1):
                pre = pre.next
            
            new_node.next = pre.next
            pre.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._len:
            return
        
        self._len -= 1
        
        if index == 0:
            self._first = self._first.next
        else:
            pre = self._first
            for _ in range(index-1):
                pre = pre.next
            
            pre.next = pre.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)