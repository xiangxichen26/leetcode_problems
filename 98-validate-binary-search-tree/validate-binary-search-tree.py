# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def postorderTraversal(root, min_v, max_v):
            if root == None:
                return True
            
            if not postorderTraversal(root.left, min_v, root.val):
                return False

            if not postorderTraversal(root.right, root.val, max_v):
                return False
            
            if root.val >= max_v or root.val <= min_v:
                return False
            return True

        return postorderTraversal(root, float('-inf'), float('inf'))