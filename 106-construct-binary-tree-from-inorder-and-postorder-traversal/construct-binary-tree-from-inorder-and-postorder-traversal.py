# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def createTree(inorder, postorder,n):
            if n == 0:
                return None
            
            # find the index of root
            k = inorder.index(postorder[n-1])
            node = TreeNode(inorder[k])
            node.right = createTree(inorder[k+1:],postorder[k:n-1],n-k-1)
            node.left = createTree(inorder[0:k],postorder[0:k],k)
            return node
        
        return createTree(inorder,postorder,len(inorder))