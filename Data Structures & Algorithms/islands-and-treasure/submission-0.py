class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])

        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        directions = ((1,0),(0,1),(-1,0),(0,-1))


        while queue:
            lr , lc = queue.popleft()
            for r, c in directions:
                nr, nc = lr + r , lc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:

                    grid[nr][nc] = grid[lr][lc] + 1
                    queue.append((nr,nc))

    

                








