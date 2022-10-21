class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(r = sr, c = sc):
            check_color = image[r][c]
            if check_color == color:
                return
            
            image[r][c] = color

            if r + 1 < len(image) and image[r + 1][c] == check_color:
                dfs(r + 1, c)
            if c + 1 < len(image[0]) and image[r][c + 1] == check_color:
                dfs(r, c + 1)
            if r - 1 >= 0 and image[r - 1][c] == check_color:
                dfs(r - 1, c)
            if c - 1 >= 0 and image[r][c - 1] == check_color:
                dfs(r, c - 1)
            

        dfs()
        return image