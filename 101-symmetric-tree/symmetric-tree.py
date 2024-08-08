# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = collections.deque([root])
        res = []

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if not cur:
                    level.append(" ")
                    continue

                level.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                else:
                    queue.append(None)
            
                if cur.right:
                    queue.append(cur.right)
                else:
                    queue.append(None)
            
            if level != level[::-1]:
                return False
        
        return True

        