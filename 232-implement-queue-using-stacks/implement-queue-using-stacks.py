
############################################################

# Write code in file solution.py

# Post solution.py in Canvas along with 4 screen shots that shows Leetcode has�

#passed. We will not use screen shot to give 100

# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass

# Note that you should do 4 times in 225, 235,622 and 641

# TA will run solution.py file 4 times in 225, 235,622 and 641

# All tests must pass for 100

###########################################################

class ListNode:

    # NOTHING CAN BE CHANGED HERE

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next



############################################################

# class Slist

###########################################################
class Slist:

    def __init__(self):

        self._head = None

        self._tail = None

        self._size = 0



    def push(self, val):

        new_node = ListNode(val)

        if self._head is None:

            self._head = self._tail = new_node

        else:

            new_node.next = self._head

            self._head = new_node

        self._size += 1



    def pop(self):

        if self._head is None:

            return None

        val = self._head.val

        self._head = self._head.next

        self._size -= 1

        if self._head is None:

            self._tail = None

        return val



    def top(self):

        return None if self._head is None else self._head.val



    def push_back(self, val):

        new_node = ListNode(val)

        if self._head is None:

            self._head = self._tail = new_node

        else:

            self._tail.next = new_node

            self._tail = new_node

        self._size += 1



    def pop_front(self):

        if self._head is None:

            return None

        val = self._head.val

        self._head = self._head.next

        self._size -= 1

        if self._head is None:

            self._tail = None

        return val



    def peek_front(self):

        return None if self._head is None else self._head.val



    def push_back_circular_queue(self, val):

        new_node = ListNode(val)

        if self._tail is None:

            self._head = self._tail = new_node

            new_node.next = self._head

        else:

            new_node.next = self._head

            self._tail.next = new_node

            self._tail = new_node

        self._size += 1



    def pop_front_circular_queue(self):

        if self._head is None:

            return False

        if self._head == self._tail:

            self._head = self._tail = None

        else:

            self._tail.next = self._head.next

            self._head = self._head.next

        self._size -= 1

        return True



    def insert_front_Circular_Deque(self, val):

        new_node = ListNode(val)

        if self._head is None:

            self._head = self._tail = new_node

        else:

            new_node.next = self._head

            self._head = new_node

        self._size += 1



    def insert_last_Circular_Deque(self, val):

        new_node = ListNode(val)

        if self._tail is None:

            self._head = self._tail = new_node

        else:

            self._tail.next = new_node

            self._tail = new_node

        self._size += 1



    def delete_front_Circular_Deque(self):

        if self._head is None:

            return False

        if self._head == self._tail:

            self._head = self._tail = None

        else:

            self._head = self._head.next

        self._size -= 1

        return True



    def delete_last_Circular_Deque(self):

        if self._head is None:

            return False

        if self._head == self._tail:

            self._head = self._tail = None

        else:

            current = self._head

            while current.next != self._tail:

                current = current.next

            current.next = None

            self._tail = current

        self._size -= 1

        return True



    def get_front(self):

        return -1 if self._head is None else self._head.val



    def get_rear(self):

        return -1 if self._tail is None else self._tail.val



    def length(self):

        return self._size



    def is_empty(self):

        return self._size == 0



############################################################

# class MyStack

###########################################################

class MyStack:

    def __init__(self):

        self._stack = Slist()



    def push(self, x: int) -> None:

        self._stack.push(x)



    def pop(self) -> int:

        return self._stack.pop()



    def top(self) -> int:

        return self._stack.top()



    def empty(self) -> bool:

        return self._stack.is_empty()



############################################################

# class MyQueue

###########################################################

class MyQueue:

    def __init__(self):

        self._queue = Slist()



    def push(self, x: int) -> None:

        self._queue.push_back(x)



    def pop(self) -> int:

        return self._queue.pop_front()



    def peek(self) -> int:

        return self._queue.peek_front()



    def empty(self) -> bool:

        return self._queue.is_empty()



############################################################

# class MyCircularQueue

###########################################################

class MyCircularQueue:

    def __init__(self, k: int):

        self._capacity = k

        self._circular_queue = Slist()



    def enQueue(self, value: int) -> bool:

        if self.isFull():

            return False

        self._circular_queue.push_back_circular_queue(value)

        return True



    def deQueue(self) -> bool:

        return self._circular_queue.pop_front_circular_queue()



    def Front(self) -> int:

        return self._circular_queue.get_front()



    def Rear(self) -> int:

        return self._circular_queue.get_rear()



    def isEmpty(self) -> bool:

        return self._circular_queue.is_empty()



    def isFull(self) -> bool:

        return self._circular_queue.length() == self._capacity



############################################################

# class MyCircularDeque

###########################################################

class MyCircularDeque:

    def __init__(self, k: int):

        self._capacity = k

        self._deque = Slist()



    def insertFront(self, value: int) -> bool:

        if self.isFull():

            return False

        self._deque.insert_front_Circular_Deque(value)

        return True



    def insertLast(self, value: int) -> bool:

        if self.isFull():

            return False

        self._deque.insert_last_Circular_Deque(value)

        return True



    def deleteFront(self) -> bool:

        return self._deque.delete_front_Circular_Deque()



    def deleteLast(self) -> bool:

        return self._deque.delete_last_Circular_Deque()



    def getFront(self) -> int:

        return self._deque.get_front()



    def getRear(self) -> int:

        return self._deque.get_rear()



    def isEmpty(self) -> bool:

        return self._deque.is_empty()



    def isFull(self) -> bool:

        return self._deque.length() == self._capacity



