# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode = root, sum_tree: int = 0):
            if not node:
                return sum_tree

            sum_tree += node.val + dfs(node.left) + dfs(node.right) if high>= node.val >= low else dfs(node.left) + dfs(node.right)
            return sum_tree
        
        return dfs()
        

            