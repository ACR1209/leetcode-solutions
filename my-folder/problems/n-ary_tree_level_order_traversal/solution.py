"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        def get_as_list(root, level):
            if root == None:
                return
            
            if(len(result) <= level ):
                for i in range(len(result), level + 1):
                    result.append([])
            
            result[level].append(root.val)
            
            for child in root.children:
                get_as_list(child, level + 1)

        get_as_list(root, 0)
        return result