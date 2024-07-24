# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
       
        res = []     
        startnode = None
        prev = None
        lastnode = None
        
        def dfs(root):
            nonlocal res, startnode, prev, lastnode
            if not root:
                return 
            # go to left  (inorder step 1)  
            dfs(root.left)
			
            # do processing....(inorder step 2)
			# get the first node where the sorted order is broken the first time and the last time
            if prev and prev.val > root.val:
                if not startnode:
                    startnode = prev
                lastnode = root
                
            prev = root
			
            # go to right (inorder step 3)    
            dfs(root.right)
            
        
        dfs(root)
        # swap the nodes that are not in place
        if startnode and lastnode:
            startnode.val, lastnode.val = lastnode.val, startnode.val
        