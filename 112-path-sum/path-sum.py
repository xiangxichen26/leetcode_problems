# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPath(self, root, path, target) -> bool:
        if not root:
            return
        
        path.append(root.val)

        if not root.left and not root.right:
            if sum(path) == target:
                return True
        
        if self.findPath(root.left,path,target):
            return True
        if self.findPath(root.right,path,target):
            return True
        path.pop()

        return False


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []

        if not root:
            return False
        return self.findPath(root,path,targetSum)

        