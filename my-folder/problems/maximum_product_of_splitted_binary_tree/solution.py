class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        subtreeSums = set()
        
        def getSum(node):
            if not node:
                return 0
            elif not node.left and not node.right:
                subtreeSums.add(node.val)
                return node.val
            else:
                result = getSum(node.left) + getSum(node.right) + node.val
                subtreeSums.add(result)
                return result
            
        rootSum = getSum(root)
        idealSplit = rootSum/2
        closestToIdeal = 0
        
        for possibleSum in subtreeSums:
            if math.fabs(possibleSum - idealSplit) < math.fabs(closestToIdeal - idealSplit):
                closestToIdeal = possibleSum        
        
        return (((rootSum - closestToIdeal) % (10**9 + 7)) * (closestToIdeal % (10**9 + 7)))  % (10**9 + 7)