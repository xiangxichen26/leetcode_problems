
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
    
    def is_empty(self):
        return self._len == 0

    def append(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("pop from empty list")
        value = self._first.val
        self._first = self._first.next
        self._len -= 1
        if self.is_empty():
            self._last = None
        return value

    def pop_back(self):
        if self.is_empty():
            raise IndexError("pop from empty list")
        if self._len == 1:
            value = self._first.val
            self._first = None
            self._last = None
        else:
            current = self._first
            while current.next != self._last:
                current = current.next
            value = self._last.val
            self._last = current
            self._last.next = None
        self._len -= 1
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._first.val

    def back(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._last.val

    def __len__(self):
        return self._len

  
  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()
        
    #############################
    # WRITE All public functions BELOW
    #############################
    
    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        return self._s.pop_back()

    def top(self) -> int:
        return self._s.back()

    def empty(self) -> bool:
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
        
    #############################
    # WRITE All public functions BELOW
    #############################

    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        return self._s.pop_front()

    def peek(self) -> int:
        return self._s.front()

    def empty(self) -> bool:
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
        
    #############################
    # WRITE All public functions BELOW
    #############################

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._s.pop_front()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.front()

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.back()

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return len(self._s) == self._K

 


###########################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
        
#############################
# WRITE All public functions BELOW
#############################

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        new_node.next = self._s._first
        self._s._first = new_node
        if self._s.is_empty():
            self._s._last = new_node
        self._s._len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._s.pop_front()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self._s.pop_back()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.front()

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.back()

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return len(self._s) == self._K
 
