# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inOrder(root: TreeNode):
            if not root:
                return 
            
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return res
            
        