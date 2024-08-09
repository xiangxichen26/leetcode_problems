"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        ans = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()

                for i in cur.children:
                    queue.append(i)
                    
            ans += 1
        return ans
        