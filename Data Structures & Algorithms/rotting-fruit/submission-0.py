class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid) , len(grid[0])
        
        q = deque([])
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1
        

        minutes = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        seen = set()
        while q and fresh > 0:
            for _ in range(len(q)):
                x,y = q.popleft()
                for row,col in directions:
                    nx,ny = row + x , col+y
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx,ny)not in seen:
                        q.append((nx,ny))
                        seen.add((nx,ny))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1

