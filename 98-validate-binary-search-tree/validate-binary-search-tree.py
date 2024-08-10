# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, min_x, max_x) -> bool:
            if not node:
                return True
            
            if not inorder(node.left, min_x, node.val):
                return False
            
            if node.val <= min_x or node.val >= max_x:
                return False

            if not inorder(node.right, node.val, max_x):
                return False

            return True
        
        return inorder(root,float("-inf"),float("inf"))

        