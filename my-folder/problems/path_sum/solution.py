# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        ans = False
        
        def dfs(node, path = [], l = 0):
            nonlocal ans
            if not node:
                return 
            
            if len(path) > l:
                path[l] = node.val
            else:
                path.append(node.val)

            
            l += 1
            
            if not node.left and not node.right:
                if sum(path[:l]) == targetSum:
                    ans = True
                    return True
                return
            
            if node.left:
                dfs(node.left, path, l)
            if node.right:
                dfs(node.right, path, l)
        dfs(root) 
        return ans
            