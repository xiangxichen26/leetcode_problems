# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack =[root]
        res=[]

        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

        return res
            
        