class ListNode:
    def __init__(self, k:int, v:int):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0
    
    # add the Node at the end
    # time complexity: O(1)
    def addLast(self, node: ListNode):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self._size += 1

    # delete a Node(Random)
    # time complexity: O(1)
    def remove(self, node:ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
    
    # delete the Node at the front
    # time complexity: O(1)
    def removeFirst(self) -> ListNode:
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    # get the size
    def size(self) -> int:
        return self._size


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cache = DoubleLinkedList()
        self.cap = capacity

    def updateRecent(self, key: int):
        # check if the key exsit
        if key not in self.map:
            return 
        # delete the node
        self.cache.remove(self.map[key])
        # add to the last
        self.cache.addLast(self.map[key])

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.updateRecent(key)
        return self.map[key].val
        
    def put(self, key: int, value: int) -> None:
        # if key in the map: update the val ,then move it to the last
        if key in self.map:
            self.map[key].val = value
            self.updateRecent(key)
        # if the key not in the map
        else:
            new_node = ListNode(key,value)
            # check if the cache has been full
            if self.cache.size() == self.cap:
                # remove the least recently
                deletedNode = self.cache.removeFirst()
                self.map.pop(deletedNode.key)
                # add to the last
            self.cache.addLast(new_node)
            self.map[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)