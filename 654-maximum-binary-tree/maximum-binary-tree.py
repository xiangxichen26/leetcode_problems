# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(arr:List,n) -> TreeNode:
            if n==0:
                return None
            max_val = max(arr)
            k = arr.index(max_val)
            node = TreeNode(max_val)    
            
            node.left = buildTree(arr[0:k],k)
            node.right = buildTree(arr[k+1:],n-k-1)
            
            return node
        
        return buildTree(nums,len(nums))
        