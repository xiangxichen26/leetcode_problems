"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def post(root):
            if not root:
                return
            
            for i in root.children:
                post(i)
            res.append(root.val)
        
        post(root)
        return res