# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# use Stack
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack =[root]
        res=[]

        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
            

        return res[::-1]
            