# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(arr:List) -> TreeNode:
            max_val = max(arr)
            k = arr.index(max_val)
            node = TreeNode(max_val)    
            
            if k == 0:
                node.left = None
            else:
                node.left = buildTree(arr[0:k])
            
            if  k == len(arr) -1:
                node.right = None
            else:
                node.right = buildTree(arr[k+1:])
            
            return node
        
        return buildTree(nums)
        