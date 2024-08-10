# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = collections.deque([(root, float('-inf'), float('inf'))])

        while queue:
            for _ in range(len(queue)):
                cur, min_x, max_x = queue.popleft()

                if cur.val >= max_x or cur.val <= min_x:
                    return False
                
                if cur.left:
                    queue.append((cur.left, min_x, cur.val))
                if cur.right:
                    queue.append((cur.right, cur.val, max_x))
        return True