# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def createTree(preorder,inorder,n):
            if n == 0:
                return None
            
            k = inorder.index(preorder[0])
            node = TreeNode(inorder[k])
            node.left = createTree(preorder[1:k+1],inorder[0:k],k)
            node.right = createTree(preorder[k+1:],inorder[k+1:],n-k-1)
            return node
        return createTree(preorder,inorder,len(inorder))
        