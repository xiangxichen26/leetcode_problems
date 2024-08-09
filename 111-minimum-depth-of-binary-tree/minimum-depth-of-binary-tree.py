# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def getDepth(node) -> int:
            if not node:
                return 0
            
            leftDepth = getDepth(node.left)  # 左
            rightDepth = getDepth(node.right)  # 右
            
            # 当一个左子树为空，右不为空，这时并不是最低点
            if node.left is None and node.right is not None:
                return 1 + rightDepth
            
            # 当一个右子树为空，左不为空，这时并不是最低点
            if node.left is not None and node.right is None:
                return 1 + leftDepth
        
            result = 1 + min(leftDepth, rightDepth)
            
            return result
        
        return getDepth(root)

