# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # can't find the node
        if not root:
            return root
        # find the val
        if root.val == key:
            # left child == None and right child == None, return None
            if not root.left and not root.right:
                return None
            # left child == None and right child != None, return root.right
            elif not root.left:
                return root.right
            # left child != None and right child == None, return root.left
            elif not root.right:
                return root.left
            # left child != None and right child != None, 
            # put the left subtree to the most left leaf node of right subtree
            else:
                cur = root.right
                # find the most left leaf node on the left subtree of the right subtree
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
            
        if key < root.val:
            # recurse the left subtree
            root.left = self.deleteNode(root.left,key)
            
        if key > root.val:
            # recurse the right subtree
            root.right = self.deleteNode(root.right,key)
        
        return root
        



        