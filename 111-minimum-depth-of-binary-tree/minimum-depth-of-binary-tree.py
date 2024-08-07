# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        queue = collections.deque([root])
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if (not cur.left) and (not cur.right):
                    return ans

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return ans

