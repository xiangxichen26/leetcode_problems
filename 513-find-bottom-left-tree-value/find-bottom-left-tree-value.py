# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = collections.deque([root])
        
        res = []
        count = 0 
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            res.append(level)
            count += 1
        
        return res[count-1][0]

        