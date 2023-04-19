# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, left_count = 0,right_count = 0):
            if not node:
                return max(left_count,right_count) - 1
            
            left_max = dfs(node.left,0,left_count+1)
            right_max = dfs(node.right,right_count+1,0)
            return max(left_max,right_max)
        
        return dfs(root)

            
