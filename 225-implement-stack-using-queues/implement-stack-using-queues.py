class ListNode:
    # NOTHING CAN BE CHANGED HERE
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

############################################################
#  class  Slist
###########################################################
class Slist():
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0

    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################

    def append_node(self, val):
        new_node = ListNode(val)
        if self._len == 0:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    def insert_front_node(self, val):
        new_node = ListNode(val)
        if self._len == 0:
            self._first = new_node
            self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node
        self._len += 1

    def remove_first(self):
        if self._len == 0:
            return None
        removed_value = self._first.val
        self._first = self._first.next
        self._len -= 1
        if self._len == 0:
            self._last = None
        return removed_value

    def remove_last(self):
        if self._len == 0:
            return None
        if self._len == 1:
            return self.remove_first()

        current = self._first
        while current.next != self._last:
            current = current.next
        removed_value = self._last.val
        self._last = current
        self._last.next = None
        self._len -= 1
        return removed_value

    def get_first(self):
        return self._first.val if self._first else None

    def get_last(self):
        return self._last.val if self._last else None

    def get_size(self):
        return self._len

    def is_empty(self):
        return self._len == 0


############################################################
#  class  MyStack
# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x):
        self._s.append_node(x)

    def pop(self):
        return self._s.remove_last()

    def top(self):
        return self._s.get_last()

    def empty(self):
        return self._s.is_empty()


############################################################
#  class  MyQueue
# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x):
        self._s.append_node(x)

    def pop(self):
        return self._s.remove_first()

    def peek(self):
        return self._s.get_first()

    def empty(self):
        return self._s.is_empty()


############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 
class MyCircularQueue:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()

    def enQueue(self, value):
        if self._s.get_size() < self._K:
            self._s.append_node(value)
            return True
        return False

    def deQueue(self):
        if not self._s.is_empty():
            self._s.remove_first()
            return True
        return False

    def Front(self):
        return self._s.get_first() if not self._s.is_empty() else -1

    def Rear(self):
        return self._s.get_last() if not self._s.is_empty() else -1

    def isEmpty(self):
        return self._s.is_empty()

    def isFull(self):
        return self._s.get_size() == self._K


############################################################
#  MyCircularDeque
# 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque
###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()

    def insertFront(self, value):
        if self._s.get_size() < self._K:
            self._s.insert_front_node(value)
            return True
        return False

    def insertLast(self, value):
        if self._s.get_size() < self._K:
            self._s.append_node(value)
            return True
        return False

    def deleteFront(self):
        return self._s.remove_first() is not None

    def deleteLast(self):
        return self._s.remove_last() is not None

    def getFront(self):
        return self._s.get_first() if not self._s.is_empty() else -1

    def getRear(self):
        return self._s.get_last() if not self._s.is_empty() else -1

    def isEmpty(self):
        return self._s.is_empty()

    def isFull(self):
        return self._s.get_size() == self._K
