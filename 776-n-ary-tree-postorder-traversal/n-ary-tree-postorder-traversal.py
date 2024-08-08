"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            n= stack.pop()
            res.append(n.val)

            for i in n.children:
                stack.append(i)

        return res[::-1]