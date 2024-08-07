"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = collections.deque([root])

        while queue:
            n = len(queue)
            pre = None
            for i in range(n):
                cur = queue.popleft()
                cur.next = pre
                pre = cur
            
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)

        return root        