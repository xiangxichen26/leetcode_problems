class ListNode:
    # NOTHING CAN BE CHANGED HERE
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Slist:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0

    def append(self, val):
        new_node = ListNode(val)
        if self._last is None:
            self._first = self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    def pop(self):
        if self._first is None:
            raise IndexError("Pop from empty list")
        val = self._first.val
        self._first = self._first.next
        if self._first is None:
            self._last = None
        self._len -= 1
        return val

    def peek(self):
        if self._first is None:
            raise IndexError("Peek from empty list")
        return self._first.val

    def is_empty(self):
        return self._len == 0

    def size(self):
        return self._len

############################################################
# 225. Implement Stack using Queues
############################################################
from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        # Reverse the queue order after each push to simulate stack behavior
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue
    

############################################################
# 232. Implement Queue using Stacks
############################################################
class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def pop(self):
        self._move_input_to_output()
        return self.output_stack.pop()

    def peek(self):
        self._move_input_to_output()
        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack

    def _move_input_to_output(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


############################################################
# 622. Design Circular Queue
############################################################
class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size


############################################################
# 641. Design Circular Deque
############################################################
class MyCircularDeque:

    def __init__(self, k):
        self.queue = [0] * k
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.max_size) % self.max_size
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.max_size) % self.max_size
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

