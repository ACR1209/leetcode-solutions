class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = [-1] * len(grid[0])
        def findBallDrop(row, col):
            if row == len(grid):
                return col
            
            nextCol = col + grid[row][col]
            
            if nextCol < 0 or nextCol > len(grid[0]) - 1 or grid[row][col] != grid[row][nextCol]:
                return -1
            
            return findBallDrop(row + 1, nextCol)
        
        for i in range(len(grid[0])):
            res[i] = findBallDrop(0, i)
        
        return res
        
