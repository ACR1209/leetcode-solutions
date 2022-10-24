# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        isBalanced = True
        
        def find_depth(node = root):
            nonlocal isBalanced
            if not node:
                return 0
            
            l, r = find_depth(node.left), find_depth(node.right)
            if abs(l - r) > 1:
                isBalanced = False
            
            return max(l, r) + 1
        
        find_depth()
        return isBalanced
            
        
        
        
