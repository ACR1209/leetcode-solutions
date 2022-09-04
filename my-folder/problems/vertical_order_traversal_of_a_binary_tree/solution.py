# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []    
        vals = []
        def preorder(root, x, y):
          if not root: return
          vals.append((x, y, root.val))
          preorder(root.left, x - 1, y + 1)
          preorder(root.right, x + 1, y + 1)
        preorder(root, 0, 0)    
        ans = []
        last_x = -1000
        for x, y, val in sorted(vals):
          if x != last_x:
            ans.append([])
            last_x = x
          ans[-1].append(val)
        return ans