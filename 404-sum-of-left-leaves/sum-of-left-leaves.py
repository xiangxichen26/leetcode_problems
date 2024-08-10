# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        leftValue = self.sumOfLeftLeaves(root.left)
        
        if root.left and not root.left.left and not root.left.right:
            leftValue = root.left.val
        
        rightValue = self.sumOfLeftLeaves(root.right)

        sum_val = leftValue + rightValue 
        
        return sum_val

        
        
        