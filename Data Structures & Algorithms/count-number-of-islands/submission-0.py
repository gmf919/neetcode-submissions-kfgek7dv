class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])


        def dfs(x, y):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':

                grid[x][y] = '0'

                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
            
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    res += 1
                    dfs(row,col)
                    
        return res


