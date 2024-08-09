"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def getDepth(root) -> int:
            if not root:
                return 0
            
            height = 0
            for i in root.children:
                new_height = getDepth(i)
                if new_height > height:
                    height = new_height
            
            return height + 1
        
        return getDepth(root)
        
    