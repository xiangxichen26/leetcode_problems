
############################################################
# Write code in file solution.py 
# Post� solution.py in Canvas along with 4 screen shots that shows Leetcode has passed. We will not use screen shot to give 100
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run solution.py file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    
    # Check if the list is empty
    class _DListNode:
        # Private node class for doubly linked list
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def is_empty(self):
        return self._len == 0

    def __len__(self):
        return self._len

    def append(self, val):
        new_node = self._DListNode(val)
        if self.is_empty():
            self._first = self._last = new_node
        else:
            new_node.prev = self._last
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    def prepend(self, val):
        new_node = self._DListNode(val)
        if self.is_empty():
            self._first = self._last = new_node
        else:
            new_node.next = self._first
            self._first.prev = new_node
            self._first = new_node
        self._len += 1

    def pop_front(self):
        if self.is_empty():
            return None
        val = self._first.val
        if self._len == 1:
            self._first = self._last = None
        else:
            self._first = self._first.next
            self._first.prev = None
        self._len -= 1
        return val

    def pop_back(self):
        if self.is_empty():
            return None
        val = self._last.val
        if self._len == 1:
            self._first = self._last = None
        else:
            self._last = self._last.prev
            self._last.next = None
        self._len -= 1
        return val

    def get_front(self):
        if self.is_empty():
            return None
        return self._first.val

    def get_back(self):
        if self.is_empty():
            return None
        return self._last.val
  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()
    
    def push(self, x):
        self._s.prepend(x)

    def pop(self):
        return self._s.pop_front()

    def top(self):
        return self._s.get_front()

    def empty(self):
        return self._s.is_empty()

############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()
    
    def push(self, x):
        self._s.append(x)

    def pop(self):
        return self._s.pop_front()

    def peek(self):
        return self._s.get_front()

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
    
    def enQueue(self, value: int) -> bool:
        if len(self._s) < self._K:
            self._s.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self._s.is_empty():
            return False
        self._s.pop_front()
        return True

    def Front(self) -> int:
        val = self._s.get_front()
        return val if val is not None else -1

    def Rear(self) -> int:
        val = self._s.get_back()
        return val if val is not None else -1

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return len(self._s) == self._K

############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
    
    def insertFront(self, value: int) -> bool:
        if len(self._s) < self._K:
            self._s.prepend(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self._s) < self._K:
            self._s.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self._s.is_empty():
            return False
        self._s.pop_front()
        return True

    def deleteLast(self) -> bool:
        if self._s.is_empty():
            return False
        self._s.pop_back()
        return True

    def getFront(self) -> int:
        val = self._s.get_front()
        return val if val is not None else -1

    def getRear(self) -> int:
        val = self._s.get_back()
        return val if val is not None else -1

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return len(self._s) == self._K
