# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def findPath(root, path, res):
            if not root:
                return 
            
            path.append(root.val)
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    res.append(path[:])
            
            if root.left:
                findPath(root.left,path,res)
                path.pop()
            if root.right:
                findPath(root.right,path,res)
                path.pop()
        
        path = []
        res = []
        findPath(root,path,res)
        return res

        