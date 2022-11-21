class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
       rows, cols = len(maze), len(maze[0])
       maze[entrance[0]][entrance[1]] = "+"

       directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
       q = collections.deque()
       q.append([entrance[0], entrance[1], 0])

       while q:
           c_row, c_col, c_dis = q.popleft()

           for d in directions:
               n_row = c_row + d[0]
               n_col = c_col + d[1]

               if 0 <= n_row < rows and 0 <= n_col < cols \
and maze[n_row][n_col] == ".":
                    
                    # If this empty cell is an exit, return distance + 1.
                    if 0 == n_row or n_row == rows - 1 or 0 == n_col or n_col == cols - 1:
                        return c_dis + 1
                    
                    # Otherwise, add this cell to 'q' and mark it as visited.
                    maze[n_row][n_col] = "+"
                    q.append([n_row, n_col, c_dis + 1])
       return -1

