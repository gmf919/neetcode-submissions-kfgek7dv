class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        maxA = 0
        seen = set()

        def dfs(x,y):

            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != 1 or (x,y) in seen:
                return 0

            seen.add((x,y))

            return 1 + dfs(x + 1,y) + dfs(x - 1,y) + dfs(x,y + 1) + dfs(x,y - 1)


            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row,col)
                    if area > maxA:
                        maxA = area

        return maxA

            


