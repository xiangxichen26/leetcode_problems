
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
    def append(self,val):
        next_node = ListNode(val)
        if not self._first:
            self._first = self._last = next_node
        else:
            self._last.next = next_node
            self._last = next_node
        self._len += 1

    def pop(self):
        if self._first is None:
            raise IndexError("Pop invalid for empty list")
        current = self._first
        if self._first == self._last:
            val = self._first.val
            self._first = self._last = None
        else:
            while current.next != self._last:
                current = current.next
            val = self._last.val
            self._last = current
            self._last.next = None
        self._len -= 1
        return val

    def is_empty(self):
        return self._len == 0

    def peek(self):
        if not self._last:
            raise IndexError("No element to peek")
        return self._last.val

    def __len__(self):
        return self._len

    def pop_first(self):
        if not self._first:
            return None
        value = self._first.val
        self._first = self._first.next
        self._len -= 1
        if not self._first:
            self._last = None
        return value

    def get_first(self):
        if not self._first:
            return None  # or raise an exception if you prefer
        return self._first.val
        
            
        
  
  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x)->None:
        self._s.append(x)

    def pop(self):
        return self._s.pop()

    def top(self):
        return self._s.peek()

    def empty(self):
        return self._s.is_empty()
        

    


############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x):
        stack2 = Slist()
        while not self._s.is_empty():
            stack2.append(self._s.pop())
        self._s.append(x)
        while not stack2.is_empty():
            self._s.append(stack2.pop())

    def pop(self):
        return self._s.pop()

    def peek(self):
        return self._s.peek()

    def empty(self):
        return self._s.is_empty()


############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    def enQueue(self, value: int) -> bool:
        if len(self._s) < self._K:
            self._s.append(value)
            return True
        return False
        
    def deQueue(self) -> bool:
        if not self._s.is_empty():
            self._s.pop_first()  # Assuming Slist has a pop_first method
            return True
        return False

    def Front(self) -> int:
        if not self._s.is_empty():
            return self._s.get_first()  # Assuming Slist has a get_first method
        return -1

    def Rear(self) -> int:
        if not self._s.is_empty():
            return self._s.peek()
        return -1

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
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    def insertFront(self, value):
        if self._s._len < self._K:
            return True
        return False

    def insertLast(self, value):
        if self._s._len < self._K:
            self._s.append(value)
            return True
        return False

    def deleteFront(self):
        if self._s.is_empty():
            return False
            
        return True

    def deleteLast(self):
        if self._s.is_empty():
            return False
        self._s.pop()
        return True

    def getFront(self):
        if self._s.is_empty():
            return -1
            
        return self._s.peek()

    def getRear(self):
        if self._s.is_empty():
            return -1
        return self._s.peek()

    def isEmpty(self):
        return self._s.is_empty()

    def isFull(self):
        return self._s._len == self._K
