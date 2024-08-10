# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self,root:TreeNode) -> int:
        if not root:
            return 0
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight ==-1 or rightHeight ==-1 or abs(leftHeight-rightHeight) > 1:
            return -1
        else:
            # return the height of this root node
            return 1 + max(leftHeight,rightHeight)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) == -1:
            return False
        return True
        
        
