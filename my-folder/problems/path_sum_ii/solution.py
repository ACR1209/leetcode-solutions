# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, path=[], path_sum=0):
            if not node:
                return
            if not node.left and not node.right and path_sum + node.val == targetSum:
                return res.append(path + [node.val])
            
            
            if node.left:
                dfs(node.left, path + [node.val], path_sum + node.val)
            if node.right:
                dfs(node.right, path + [node.val], path_sum + node.val)
            
        dfs(root)
        return res