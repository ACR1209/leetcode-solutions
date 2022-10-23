# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0
        
        def find_path(node=root, path = [], l = 0):
            nonlocal good
            if not node:
                return
        
            if l < len(path):
                path[l] = node.val
            else:
                path.append(node.val)
            
            if max(path[:l + 1]) == node.val:
                good += 1
            
            if node.right:
                find_path(node.right, path, l + 1)
            if node.left:
                find_path(node.left, path, l + 1)
    
        find_path()
        return good