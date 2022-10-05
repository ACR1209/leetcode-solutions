# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def add_dfs(node = root, d = 1):

            if not node:
                return 
            
            if depth - 1 == 0:
                nonlocal root

                new = TreeNode(val, root)
                root = new
                return 
            
            if depth - 1 == d:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return 
               
            add_dfs(node.left, d + 1)
            add_dfs(node.right, d + 1)
            
        add_dfs() 
        return root
