# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def contains(node):
            if not node:
                return False
        
            if not contains(node.left):
                node.left = None

            if not contains(node.right):
                node.right = None

            return node.val or node.left or node.right
        
        return root if contains(root) else None